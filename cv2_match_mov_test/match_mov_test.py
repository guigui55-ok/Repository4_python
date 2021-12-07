from enum import Flag
import cv2

from numpy import result_type, true_divide
import import_init


import common_util.log_util.logger_init as logger_init
import common_util.log_util.logging_util as logging_util
import common_util.cv2_image.cv2_find_image_util as cv2_find_image_util
import common_util.cv2_image.cv2_movie as cv2_movie
import common_util.cv2_image.cv2_image_comp as cv2_image_comp
import common_util.general_util.general as general

'''
以下のような動画は正しく判定できない可能性がある
・フレーム毎に大幅にイメージが頻繁に変わるもの
・約30fpsで約0.3秒(以下)毎[1フレーム以下]で大幅にフレームイメージが変わるもの
'''

def main():    
    logger:logging_util = logger_init.initialize_logger()
    base_path = './movie/screenrecord1.mp4'
    temp_path = './movie/screenrecord1_Trim.mp4'
    temp_path = './movie/screenrecord1_Trim3.mkv'
    temp_path = './movie/screenrecord2.mp4'
    import datetime
    result_dir = './result_images' + datetime.datetime.now().strftime('%y%m_%H%M%S')
    step_sec = 0.1
    first_match_threshold = 0.8
    # mov_temp と一致したフレームから、両方の mov を比較する
    # すべて一致したらOKとなる
    is_exists = is_exists_target_movie_in_movie(
        logger,base_path,temp_path,
        step_sec,first_match_threshold,result_dir)
    return is_exists

def is_exists_target_movie_in_movie(
    logger : logging_util,
    mov_base_path : str,
    mov_temp_path : str,
    comp_step_sec : int=0.1,
    first_match_threshold : float = 0.8,
    result_dir : str = ''
    )->bool:
    """
    mov_base_path の中に mov_temp_path が存在するか判定する
    ※ フレーム数は mov_base_path ＞ mov_temp_path であることを想定
    """
    try:
        import os 
        if not os.path.exists(mov_base_path):
            logger.exp.error('mov_base_path is not exists , return False')
            return False
        if not os.path.exists(mov_temp_path):
            logger.exp.error('mov_temp_path is not exists , return False')
            return False
        
        if not( os.path.exists(result_dir) and os.path.isdir(result_dir)):
            os.mkdir(result_dir)
            logger.info('create_dir_if_nothing : mkdir , dir = ' + result_dir)

        mov_base = cv2_movie.video_capture_frames(logger,mov_base_path)
        flag = mov_base.initialize_value('base')
        if not flag:
            logger.exp.error('base_mov.initialize_value failed , return False')
            return False
        mov_temp = cv2_movie.video_capture_frames(logger,mov_temp_path)
        flag = mov_temp.initialize_value('temp')
        if not flag:
            logger.exp.error('mov_temp.initialize_value failed , return False')
            return False
        mov_base.info.show_movie_info()
        mov_temp.info.show_movie_info()

        # 開始位置に別のイメージファイルを使用する場合は
        # イメージファイルをcv2image で読み込み,start_imgへ
        # get_frame_max_match_value_by_image_compメソッドを、
        # start_img と mov_base,mov_temp へそれぞれ実行、スタート位置を渡す
        # その後、is_exists_target_movie_in_movie_for_object でそれぞれの値を渡せばOK

        # mov_temp の最初のフレームと mov_base 各フレームを比較して、
        # 一致率が最大のフレーム一と、閾値を取得する
        exists_frame_count ,threshold_max = get_frame_if_exists_target_first_frame_in_movie(
            logger,mov_base,mov_temp,first_match_threshold,result_dir)
        # first_match_threshold 以上のフレームが存在しなければ終了する
        if exists_frame_count < 0:
            logger.exp.error('is_exists_first_frame = false , return')
            return False
        # mov_temp と一致したフレームから、両方の mov を比較する
        # すべて一致したらOKとなる
        temp_begin_frame = 0
        is_exists = is_exists_target_movie_in_movie_for_object(
            logger,
            mov_base,
            exists_frame_count,
            mov_temp,
            threshold_max,
            first_match_threshold,
            temp_begin_frame,
            comp_step_sec,
            result_dir)
        logger.info('is_exists_target_movie_in_movie_for_object = ' + str(is_exists))
        return is_exists
    except Exception as e:
        logger.exp.error(e)
        return False

def is_exists_target_movie_in_movie_for_object(
    logger : logging_util,
    mov_base : cv2_movie.video_capture_frames,
    mov_base_begin_frame : int,
    mov_temp : cv2_movie.video_capture_frames,
    threshold : float = 0.9987,
    min_border_threshold : float = 0.8,
    mov_temp_begin_frame : int=0,
    step_sec : float=0.1,
    result_dir : str = ''
)->bool:
    """
    move_base の中に mov_temp が存在するか判定する
    ※ フレーム数は mov_base ＞ mov_temp であることを想定
    """
    try:
        fn = 'is_exists_target_movie_in_movie_for_object'
        general.print_now_method(is_exists_target_movie_in_movie_for_object)
        threshold_new = (threshold + min_border_threshold) /2
        # fps が異なるか最初にチェック
        is_difference_fps = False
        if mov_base.info.movie_fps != mov_temp.info.movie_fps:
            is_difference_fps = True
            # ※ fps が同じものを想定しているため
        # 比較対象位置までフレームを移動する
        mov_base.set_frame(mov_base_begin_frame)
        mov_base_begin_sec = mov_base.info.movie_spf * mov_base_begin_frame
        mov_temp.set_frame(mov_temp_begin_frame)
        mov_temp_begin_sec = mov_temp.info.movie_spf * mov_temp_begin_frame
        # 一致したカウント
        same_count:int = 0
        # 比較を実行した回数
        comp_count:int = 0
        # 進めた秒数
        sec_count:float = 0
        # 動画 frame が一致しないが、シーンが変更されたと判定された数
        scene_change_count = 0
        # result_value_avg
        result_value_avg = 0.0
        is_not_match = False
        # すべて合致するか比較する
        while(not mov_temp.frame_is_max_or_max_over()):
            # 現在のフレーム位置イメージを読み込みむ
            img_temp = mov_temp.frame_capture_now
            # print('mov_temp.frame = ' + str(mov_temp.frame_int_now))
            # イメージを結果フォルダに保存する
            filename = str(comp_count) + '_temp'
            save_image_for_mov_comp(logger,img_temp, filename,result_dir)
            is_same = False
            while(not mov_base.frame_is_max_or_max_over()):
                # 現在のフレーム位置イメージを読み込む
                img_base = mov_base.frame_capture_now
                # print('mov_base.frame = ' + str(mov_base.frame_int_now))
                # img_bae, img_temp が一致か判定する
                # is_same = cv2_image_comp.is_same_image(logger,img_base,img_temp)  
                is_same , result_value = is_same_image(logger,img_base,img_temp,threshold_new) 
                # イメージを結果フォルダに保存する
                filename = str(comp_count) + '_1_base_' + str(is_same)
                save_image_for_mov_comp(logger,img_temp, filename,result_dir)
                comp_count += 1
                if is_same :
                    same_count+=1
                else:
                    # is_same == False の時はまず fpr 違いによる動画のずれを考慮した処理をする
                    # 秒数がなるべく一致する箇所を再比較する
                    if is_difference_fps:
                        # begin_frame から進んだ秒数を算出
                        frame = mov_base.frame_int_now - mov_base_begin_frame
                        mov_base_sec_now = mov_base.info.movie_spf * frame                      
                        # begin_frame から進んだ秒数算出
                        frame = mov_temp.frame_int_now - mov_temp_begin_frame  
                        mov_temp_sec_now = mov_temp.info.movie_spf * frame
                        retry_frame:int = 0
                        if mov_base_sec_now == mov_temp_sec_now:
                            # 進んだ秒数も全く同じ場合は False
                            is_same = False
                            retry_frame = 0
                            # retry_frame = -1
                        elif mov_base_sec_now > mov_temp_sec_now:
                            # 位置をずらしてもう一度比較する 一つ前と
                            retry_frame = -1
                        elif mov_base_sec_now < mov_temp_sec_now:
                            # 位置をずらしてもう一度比較する 一つ次と
                            retry_frame = 1
                        else:
                            # ここには来ないはず
                            pass
                            logger.exp.error('unexpected case')
                        # retry 用フレームへ移動
                        if retry_frame != 0:
                            logger.info('retry : retry_frame = ' + str(retry_frame))
                            mov_base.move_frame(retry_frame)
                                        
                        img_base = mov_base.frame_capture_now
                        is_same , result_value = is_same_image(logger,img_base,img_temp,threshold_new)
                        # イメージを結果フォルダに保存する
                        filename = str(comp_count) + '_2_base_' + str(is_same)
                        save_image_for_mov_comp(logger,img_temp, filename,result_dir)
                        # フレームを元に戻す
                        if retry_frame != 0:
                            mov_base.move_frame(-int(retry_frame))

                        if is_same:
                            same_count += 1
                        else:
                            # comp_result < min_border(0.8)
                            # img_temp * img_base ：通常比較で一致しない
                            # img_temp * img_base[1or-1]：fps差異考慮で一致しない場合
                            # 前のフレームと大幅にシーンが変更されている可能性を考慮する
                            # fps にずれがある場合、temp,base のシーン変更位置にずれがある可能性がある
                            # img_base * img_base[-1] , img_temp * img_temp[-1] を比較して
                            # 大幅に異なれば、シーン変更がされている可能性があるので、この場合カウントしておく
                            if result_value < min_border_threshold:
                                # 大幅に違うときは、前のフレームと比較して、シーン変更されているか判定する
                                frame_move_pos = -1
                                # img_base
                                img_base_before = mov_base.get_video_capture_image(frame_move_pos)
                                before_comp_base_value = cv2_image_comp.get_compareist_value(
                                    logger,img_base,img_base_before)
                                # img_temp も比較する
                                img_temp_before = mov_temp.get_video_capture_image(frame_move_pos)
                                before_comp_temp_value = cv2_image_comp.get_compareist_value(
                                    logger,img_temp,img_temp_before)
                                # base , temp いずれかが前の frame と大幅に異なるときはカウントする
                                if before_comp_base_value < min_border_threshold or \
                                    before_comp_temp_value < min_border_threshold:
                                    scene_change_count += 1
                                # 位置を元に戻す → # whileの最後で sec_pos 指定するので不要
                                # mov_temp.move_frame(-frame_move_pos)
                                # mov_base.move_frame(-frame_move_pos)
                                #
                                is_same = False
                            else:
                                # comp_result > min_border(0.8)、fps_result==False
                                is_same = False
                            is_not_match = True
                    ### end if is_difference_fps
                if is_same:
                    result_value_avg += result_value
                # step_sec 分移動する
                sec_count += step_sec
                mov_base.move_sec(step_sec)
                break
            ### end while
            # step_sec 分移動する
            mov_temp.move_sec(step_sec)
            
        ### end while
        # 比較した回数と一致した回数が同じならTrue
        logger.info('count:same/comp/scean_change = ' +str(same_count) + ' / ' + str(comp_count) + ' / ' + str(scene_change_count))
        result_value_avg = result_value_avg / same_count
        logger.info('result_value_avg = ' + str(result_value_avg))
        if same_count == (comp_count - scene_change_count):
            return True
        else:
            return False
    except Exception as e:
        logger.exp.error(e)
        return False

def get_frame_if_exists_target_first_frame_in_movie(
    logger : logging_util,
    mov_base : cv2_movie.video_capture_frames,
    mov_temp : cv2_movie.video_capture_frames,
    threshold : float = 0.8,
    result_dir : str = '')-> bool:
    """mov_temp の最初のフレーム と mov_base のキャプチャを比較し、すべての中から一番一致率が高い
    フレーム一と、その時の閾値を返す
    * target : mov_temp
    戻り値：
        成功時：一致率最大時の mov_base のフレームカウントと閾値[frame,threshold]
        失敗時：一致しないときは frame,threshold [-1,1]、例外発生時は [-2,1] を返す
        ※失敗時の閾値を 0 にすると、のちの画像比較ですべてOKとなる可能性があるため、1 とする
    """
    try:
        mov_temp.set_frame(0)
        img_temp = mov_temp.frame_capture_now
        logger.info('get_frame_if_exists_target_first_frame_in_movie')
        logger.info('mov_temp.frame = ' + str(mov_temp.frame_int_now))
        # match_frame = get_frame_if_exists_image_in_movie(
        #     logger,mov_base,img_temp)
        match_frame ,threshold= get_frame_max_match_value_by_image_comp(
            logger,mov_base,img_temp,threshold,result_dir)
        
        return match_frame,threshold
    except Exception as e:
        logger.exp.error(e)
        return -3,1

def get_frame_if_exists_image_in_movie(
    logger : logging_util,
    mov_base : cv2_movie.video_capture_frames,
    img_temp , threshold :float = 0.990)-> int:
    """xxxxxxxxxxx
    img_temp が mov_base の中に存在するか(一致しているものがあるか)判定し
    一致していた場合、mov_base の一致したフレームカウントを返す
    戻り値：
        成功時：一致した mov_base のフレームカウント
        失敗時：一致しないときは -1、例外発生時は -2 を返す"""
    try:
        general.print_now_method(get_frame_if_exists_image_in_movie)
        mov_base.set_frame(0)
        from common_util.cv2_image.cv2_image_util import cv2_image
        cv2img = cv2_image(logger,img_temp)
        cv2img.save_img_with_name_auto('temp')
        while(not mov_base.frame_is_max_or_max_over()):
            img_base = mov_base.frame_capture_now()
            ## debug
            # if mov_base.frame_int_now % 100 == 0:
            #     path = './img_base' + str(mov_base.frame_int_now) + '.png'
            #     cv2.imwrite(path,img_base)
            #     print(path)
            ## NG - not match
            # is_same = cv2_image_comp.is_same_image(logger,img_base,img_temp)
            is_same = cv2_image_comp.is_same_by_calcHist(
                logger,img_base,img_temp,threshold)
            if is_same:                
                cv2img = cv2_image(logger,img_base)
                cv2img.save_img_with_name_auto('base_match')
                logger.info('get_frame_if_exists_image_in_movie : match.frame = ' + str(mov_base.frame_int_now))
                break
            # next_frame_base = mov_base.frame_int_now + 1
            # mov_base.move_frame(next_frame_base)
            mov_base.move_next()
        
        ret = 0
        if mov_base.frame_is_max_or_max_over():
            ret = -1
        else:
            ret = mov_base.frame_int_now
        return ret
    except Exception as e:
        logger.exp.error(e)
        return -2



def get_frame_max_match_value_by_image_comp(
    logger : logging_util,
    mov_base : cv2_movie.video_capture_frames,
    img_temp,
    threshold : float = 0.8,
    result_dir : str = '' )-> int:
    """img_temp と mov_base のキャプチャを比較し、すべての中から一番一致率が高い
    フレーム一と、その時の閾値を返す
    戻り値：
        成功時：一致した mov_base のフレームカウントと閾値[frame,threshold]
        失敗時：一致しないときは frame,threshold [-1,1]、例外発生時は [-2,1] を返す
        ※失敗時の閾値を 0 にすると、のちの画像比較ですべてOKとなる可能性があるため、1 とする
        """
    try:
        general.print_now_method(get_frame_if_exists_image_in_movie)
        import cv2
        if result_dir != '':
            save_image_for_mov_comp(logger,img_temp,'first_temp',result_dir)
        now_max = 0
        frame_max = 0
        while(not mov_base.frame_is_max_or_max_over()):
            # get_video_capture_image_and_move_next
            # img_base = mov_base.get_video_capture_image(0,False)
            # img_base = mov_base.get_video_capture_image_and_move_next(False)
            # 現在のフレームを取得する mov_base
            img_base = mov_base.frame_capture_now
            ## debug
            # if mov_base.frame_int_now % 100 == 0:
            #     path = './img_base' + str(mov_base.frame_int_now) + '.png'
            #     cv2.imwrite(path,img_base)
            #     print(path)
            ## NG - not match
            # is_same = cv2_image_comp.is_same_image(logger,img_base,img_temp)
            value:float = cv2_image_comp.get_compareist_value(
                logger,img_base,img_temp)
            if value > threshold:
                if now_max < value:
                    now_max = value
                    frame_max = mov_base.frame_int_now
                    logger.info('frame,max_value =' + str(frame_max) + ' , ' + str(value))
            # if is_same:                
            #     cv2img = cv2_image(logger,img_base)
            #     cv2img.save_img_with_name_auto('base_match')
            #     logger.info('get_frame_if_exists_image_in_movie : match.frame = ' + str(mov_base.frame_int_now))
            #     break
            # next_frame_base = mov_base.frame_int_now + 1
            # mov_base.move_frame(next_frame_base)
            mov_base.move_next()
        # 初回一致時のフレームをファイルへ保存する
        if result_dir != '':
            img = mov_base.get_video_capture_image(frame_max)
            save_image_for_mov_comp(logger,img,'first_base',result_dir)
        # 一致しないときは-1を返す
        if now_max == 0:
            frame_max = -1
            now_max = 1
        return frame_max , now_max
    except Exception as e:
        logger.exp.error(e)
        return -2 , 1

def save_image_for_mov_comp(logger,img,name='',result_dir=''):
    try:
        from common_util.cv2_image.cv2_image_util import cv2_image
        cv2img = cv2_image(logger,img)
        cv2img.save_img_with_name_auto(name,result_dir)
    except Exception as e:
        logger.exp.error(e)

def is_same_image(logger,img_base,img_temp,threshold):
    try:        
        result_value = cv2_image_comp.get_compareist_value(logger,img_base,img_temp)
        if result_value >= threshold:
            is_same = True
        else:
            is_same = False
        
        if is_same:
            logger.info('is_same_by_calcHist: True , '+str(threshold) + ' <= ' + str(result_value))
        else:
            logger.info('is_same_by_calcHist: False , '+str(threshold) + ' > ' + str(result_value))
        return is_same,result_value
    except Exception as e:
        logger.exp.error(e)
        return False,0.0

main()