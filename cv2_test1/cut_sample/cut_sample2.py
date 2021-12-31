from ntpath import join
import import_init
import traceback


def get_result_path():
    import common_util.general_util.general as general
    import pathlib,os
    dir_path = str(pathlib.Path(__file__).parent)
    child_dir_name = 'write_frames_result_' + general.get_datetime()
    result_path = os.path.join(dir_path,child_dir_name)
    if not os.path.exists(result_path):
        os.mkdir(result_path)
    return result_path

from common_util.cv2_image.cv2_image_util import Cv2Image
def test_cut_grid():
    try:
        logger = import_init.initialize_logger_new()
        read_dir = r'C:\Users\OK\source\repos\Repository4_python\movie_test\write_frames_test\write_frames_result_2112_072920'
        read_file_name = 'buttle2_64.png'
        read_path = import_init.path_join(read_dir,read_file_name)

        ret_dir = import_init.get_path_from_current_dir('images')
        import os 
        if not os.path.exists(ret_dir):
            pass
        else:
            import shutil
            shutil.rmtree(ret_dir)
        os.mkdir(ret_dir)
        ret_path = ''
        img_obj = Cv2Image(logger,read_path) # 書き込むためのもの
    
        # 拡張子なしのファイル名
        import os
        basename_without_ext:str = os.path.splitext(os.path.basename(read_path))[0]
        ext = '.png'
        base_file_name = basename_without_ext + ext
    
        rect = [4, 922, 716, 1516 ]
        from common_util.cv2_image.grid_data import GridTable
        table = GridTable(rect, row_max= 5, col_max= 6)

        # 基本イメージをファイルへ保存する        
        buf_img = img_obj.triming(rect)
        buf_ret_path = import_init.path_join(ret_dir,'zz_base_image.png')
        img_obj.save_img_other(buf_ret_path,buf_img)
        
        while(not table.is_over_max_index()):
            # 現在の範囲を取得
            buf_rectangle = table.get_current_rectangle()
            buf_rectangle.print_value()
            # 取得した範囲を切り取る
            buf_img = img_obj.triming(buf_rectangle.get_value_as_list())
            # ファイル名、パスを設定する
            buf_addstr = '_' + table.get_current_coordinate_str()
            buf_ret_name = basename_without_ext + buf_addstr + ext
            buf_ret_path = import_init.path_join(ret_dir,buf_ret_name)
            # イメージを保存する
            img_obj.save_img_other(buf_ret_path,buf_img)
            table.image_list.append(buf_img)
            # 次の範囲へ
            # table.move_next()
            table.current_index += 1

        return
    except:
        traceback.print_exc()

def test_cut_grid2(
    logger,
    base_img_path,
    target_rect,
    rows_count=5,
    cols_count=6,
    result_dir_path=''):
    try:
        before_cut_image_file_name = 'base_image.png'
        basename_without_ext = ''
        ext = ''
        if result_dir_path != '':
            import pathlib,os
            ret_dir = os.path.join(result_dir_path,'images')
            if not os.path.exists(ret_dir):
                os.mkdir(ret_dir) # 存在しないときは作成（dirがないと、例外が出ずにファイルが作成されない）
            else:
                pass
                # import shutil
                # shutil.rmtree(ret_dir)
                
            # 拡張子なしのファイル名
            import os
            basename_without_ext:str = os.path.splitext(os.path.basename(base_img_path))[0]
            ext = '.png'
            base_file_name = basename_without_ext + ext
        else:
            ret_dir = ''
            
        
        img_obj = Cv2Image(logger,base_img_path) # 書き込む、切り取るためのもの
        # rect = [4, 922, 716, 1516 ]
        rect = target_rect
        from common_util.cv2_image.grid_data import GridTable
        table = GridTable(rect, row_max= rows_count, col_max= cols_count)

        # 基本イメージをファイルへ保存する
        if ret_dir != '':
            buf_img = img_obj.triming(rect)
            buf_ret_path = import_init.path_join(ret_dir,before_cut_image_file_name)
            img_obj.save_img_other(buf_ret_path,buf_img)
        
        while(not table.is_over_max_index()):
            # 現在の範囲を取得
            buf_rectangle = table.get_current_rectangle()
            buf_rectangle.print_value()
            # 取得した範囲を切り取る
            buf_img = img_obj.triming(buf_rectangle.get_value_as_list())
            if basename_without_ext != '':
                # ファイル名、パスを設定する
                buf_addstr = '_' + table.get_current_coordinate_str()
                buf_ret_name = basename_without_ext + buf_addstr + ext
                buf_ret_path = import_init.path_join(ret_dir,buf_ret_name)
                # イメージを保存する
                img_obj.save_img_other(buf_ret_path,buf_img)
            # イメージをGridTableに保持する
            table.image_list.append(buf_img)
            # 次の範囲へ
            # table.move_next() # max < current とならないのでループする
            table.current_index += 1
        return
    except:
        traceback.print_exc()

test_cut_grid()