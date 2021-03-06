import cv2
from numpy import true_divide

# movie_info
# movie_play > (movie_info ,video_capture_frames)

# =============================================================================
class cv2_movie_info():
    logger = None
    movie_path = ''
    movie_width = 0
    movie_height = 0
    movie_fps = 0.0
    movie_frame_max_count = 0
    movie_time_sec = 0.0
    # 1 frame あたりの秒数 spf
    movie_spf = 0.0

    def __init__(self,logger_,movie_path_) -> None:
        self.logger = logger_
        self.movie_path = movie_path_

    def save_movie_info(self,video_capture:cv2.VideoCapture):
        try:
            self.movie_width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.movie_height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
            self.movie_fps = video_capture.get(cv2.CAP_PROP_FPS)
            self.movie_frame_max_count = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)
            self.movie_time_sec = self.movie_frame_max_count / self.movie_fps
            self.movie_spf = 1 / self.movie_fps
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False
            
    def show_movie_info(self):
        cap :cv2.VideoCapture = None
        try:
            cap = cv2.VideoCapture(self.movie_path)
            if (cap.isOpened() == False):  
                self.logger.exp.error("cv2.VideoCapture.isOpened False") 
                return False
            self.save_movie_info(cap)
            # --------------------------------
            self.logger.info(' -------  movie_info  ------- ')
            self.logger.info('movie_full_path = ' + str(self.movie_path))
            self.logger.info('movie_size[w:h] = ' + str(self.movie_width) + ' , ' + str(self.movie_height))
            self.logger.info('fps = ' + str(self.movie_fps))
            self.logger.info('frame_max_count = ' + str(self.movie_frame_max_count))
            self.logger.info('movie_time(sec) = ' + str(self.movie_time_sec))
            self.logger.info('movie_spf = ' + str(self.movie_spf))
            self.logger.info(' -------  -------  ------- ')
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False
        finally:
            try:
                if cap != None:
                    cap.release()
                cv2.destroyAllWindows()
            except Exception as e:
                self.logger.exp.error(e)
                return False

        
# =============================================================================
from enum import Enum
from enum import IntEnum
class const_play(IntEnum):
    STOP = 0
    PLAY = 1
    PAUSE = 2
    FEW = 3
    REV = 4
    EXIT = 5
    ERROR = 6
    NONE = 7
    FORWARD = 8
    REWIND = 9
    FORWARD_REWIND_SPEED_DEFAULT = 20
    CV2_NAMED_WINDOW_VALUE_DEFAULT = cv2.WINDOW_NORMAL
    CV2_NAMED_WINDOW_VALUE_DEFAULT_WINDOW_NORMAL = cv2.WINDOW_NORMAL
    CV2_WINDOW_PROPETY_VALUE1 = cv2.WND_PROP_ASPECT_RATIO
    CV2_WINDOW_PROPETY_VALUE1_WND_PROP_ASPECT_RATIO = cv2.WND_PROP_ASPECT_RATIO
    CV2_WINDOW_PROPETY_VALUE2 = cv2.WINDOW_AUTOSIZE
    CV2_WINDOW_PROPETY_VALUE2_WINDOW_AUTOSIZE = cv2.WINDOW_AUTOSIZE

# =============================================================================
class const_play_str(Enum):
    CAPTURE_FILE_NAME_DEFAULT = './movie_capture.png'
    WINDOW_TITLE_DEFAULT = 'Video'
    WINDOW_SIZE_DEFAULT = (0,0)

# =============================================================================
class movie_player_key():
    exit = 'q'
    pause_play = 'p'
    pause_play2 = ' '
    capture = 'c'
    next_frame_one = '3'
    previeous_frame_one = '1'
    rewind = '7'
    forward = '9'

class video_capture_frames():
    logger =None
    info : cv2_movie_info = None
    window_title = ''
    play_ret = None
    frame_capture_now = None
    frame_int_now = 0
    frame_int_max = 0
    video_capture : cv2.VideoCapture = None
    capture_file_name = const_play_str.CAPTURE_FILE_NAME_DEFAULT.value

    # =======================================
    def __init__(self, logger_, movie_path_:str, movie_info_:cv2_movie_info=None) -> None:
        try:
            if movie_info_ == None:
                self.logger = logger_
                self.info = cv2_movie_info(logger_,movie_path_)
                self.logger.info('movie_manager.__init__ : by movie_path_')
                self.logger.info('path = ' + movie_path_)
            else:
                self.info = movie_info_
                self.logger = movie_info_.logger
                self.logger.info('movie_manager.__init__ : by movie_info_')
                self.logger.info('path = ' + self.info.movie_path)
        except Exception as e:
            logger_.exp.error(e)
    
    def initialize_value(self,window_title) -> bool:
        try:
            self.window_title = window_title
            self.logger.info('video_capture_frames.window_title = '+ self.window_title)
            # get Capture
            #self.video_capture = cv2.VideoCapture(self.info.movie_path)
            self.start_capture()
            # read
            # self.play_ret, self.frame_capture_now = self.video_capture.read()
            self.move_next()
            # set frame_max
            self.frame_int_max = int(self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT)) 
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False
    
    def get_movie_info(self):
        try:
            if self.capture_movie == None:
                msg = self.__class__
                msg = '.get_movie_info: self.capture_movie == None , return'
                self.logger.exp.error(msg)
                return ''
            ret = ''
            self.info.show_movie_info
        except Exception as e:
            self.logger.exp.error(e)
    
    def move_mext_sec(self)->bool:
        """1秒分フレームを進める"""
        try:
            change_frame = 0
            while(change_frame>=1):
                change_frame += self.info.movie_spf
            return self.set_frame(change_frame)
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def move_sec(self,sec=1)->bool:
        """指定した秒数分フレームを進める
        1フレーム当たりの秒数の、加算を続け、sec 以上になったときの、フレームカウントを移動する
        ※ 上記処理 (および、1フレーム当たりの秒数が決まっている) のため、sec と 移動する秒数が完全に一致しない場合が多い
        """
        try:
            move_frame = self.get_frame_by_sec(sec)
            return self.move_frame(move_frame)
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def get_frame_by_sec(self,sec) -> int:
        """引数sec秒あたりのframe数を取得する"""
        try:
            if sec == 0 : return 0
            is_minors = False
            if sec < 0 : is_minors=True
            buf_sec = abs(sec)
            if buf_sec > self.info.movie_time_sec:
                ret = self.info.movie_frame_max_count
                if is_minors : ret *= -1
                return ret
            
            count_sec = 0
            count_frame = 0
            while(count_sec <= buf_sec):
                count_sec += self.info.movie_spf
                count_frame += 1
            ret = count_frame
            if is_minors : ret *= -1
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return 0
        


    def move_next(self):
        """img を video_capture.read で読み込みメンバへ格納、frame を次へ進める
        その後、update_frame_int_now"""
        try:
            self.play_ret, self.frame_capture_now = self.video_capture.read()
            self.update_frame_int_now()
        except Exception as e:
            self.logger.exp.error(e)

    def start_capture(self):
        try:
            self.video_capture:cv2.VideoCapture= cv2.VideoCapture(self.info.movie_path)
            self.update_frame_int_now()
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def get_frame_int_now(self)->int:
        """現在のフレームを取得するときはこの関数の使用を推奨
        self.frame_int_now は move_frame などの後や、
        self.frame_int_now を上書きしたときに、更新されていない可能性がある
        """
        try: 
            self.update_frame_int_now()
            return self.frame_int_now
        except Exception as e:
            self.logger.exp.error(e)
            return -1
    
    def update_frame_int_now(self)->bool:
        try:            
            self.frame_int_now = int(self.video_capture.get(cv2.CAP_PROP_POS_FRAMES))
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def set_frame_int_now(self,set_frame_count)->bool:
        try:            
            self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, set_frame_count)
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False
            
    def frame_is_over_max(self):
        frame = int(self.video_capture.get(cv2.CAP_PROP_POS_FRAMES))
        if int(frame) > self.frame_int_max:
            return True
        return False

    def frame_is_max_or_max_over(self):
        frame = int(self.video_capture.get(cv2.CAP_PROP_POS_FRAMES))
        if frame >= self.frame_int_max:
            return True
        return False

    def capture_movie(self,write_path=''):
        # 現在表示されているイメージをファイルに保存する
        try:
            write_path = self.capture_file_name 
            cv2.imwrite(write_path,self.frame_capture_now)
            self.logger.info('capture success. path= ' + write_path)
        except Exception as e:
            self.logger.exp.error(e)

    def get_video_capture_image_and_move_next(self,is_logout=True):
        """現在のフレームの captureイメージを取得して次のフレームへ移動する"""
        try:
            return self.get_video_capture_image(1,is_logout)
        except Exception as e:
            self.logger.exp.error(e)
            return None
    
    def get_video_capture_image(self,frame_pos=0,is_logout=True):
        """指定した frame 位置のイメージを取得する
        ※ 読み込んだ後 frame_pos は移動される
        ※ 読み込んだ時は、自動的に次のフレームへ移動する"""
        try:
            frame_pos = self.frame_int_now + frame_pos -1
            self.set_frame(frame_pos,is_logout)            
            # self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_pos -1 )
            # self.move_next()
            # ret,frame_now = self.video_capture.read()
            # self.update_frame_int_now()
            return self.frame_capture_now
        except Exception as e:
            self.logger.exp.error(e)
            return None

    def show_next_frame_and_pause(self,move_frame_count=1):
        """次のフレームを表示する（実行時に一時停止となる）"""
        self.move_frame(move_frame_count)

    def show_previous_frame_and_pause(self,move_frame_count=-1):
        """前のフレームを表示する（実行時に一時停止となる）"""
        self.move_frame(move_frame_count)
        
    def set_frame(self,set_frame_count=0,is_logout = True)->bool:
        """set した後に self.move_next を実行している"""
        try:
            # frame を capture へセットして読み込み、表示する
            # self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, set_frame_count)
            self.set_frame_int_now(set_frame_count)
            #self.play_ret, self.frame_int_now = self.video_capture.read()
            # cv2.imshow(self.window_title, self.frame_int_now)
            
            self.move_next()
            self.frame_int_now = self.get_frame_int_now()
            if is_logout:
                self.logger.info(
                    self.window_title + ' : frame_now = ' + str(self.frame_int_now) + ' / ' + str(self.frame_int_max))
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False
    
    def set_sec(self,set_sec:float=0) ->bool:
        """秒数を指定して、フレームをセットする"""
        try:
            set_frame_count = set_sec * self.info.movie_spf
            return self.set_frame(set_frame_count)
        except Exception as e:
            self.logger.exp.error(e)
            return False
        
    def move_frame(self,move_frame_count=0)->bool:
        """任意の位置のフレームを表示する（実行時に一時停止となる）
        現在のフレームから move_frame_count 進める
        デフォルトは1フレーム進む
        """
        try:
            # 現在の再生位置（フレーム位置）の取得
            #self.frame_int_now = int(self.video_capture.get(cv2.CAP_PROP_POS_FRAMES))
            self.update_frame_int_now()

            # 以下 read 時に1フレーム進むので、-1 する
            self.frame_int_now += move_frame_count -1

            # 最後の位置より上、ゼロより下の場合は処理を中断する
            if self.frame_int_now > self.frame_int_max \
                or self.frame_int_now  < 0:
                self.logger.info('[frame_now + move_frame_count] == [> frame_max] or [< 0] . frame_now = ' + str(self.frame_int_now))

                if self.frame_int_now  > self.frame_int_max:
                    self.frame_int_now = self.info.movie_frame_max_count
                if self.frame_int_now  < 0:
                    self.frame_int_now = 0
            
            self.set_frame(self.frame_int_now)
            # frame をセットして読み込み、表示する
            # self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, self.frame_int_now)
            # print('frame_now = ' + str(self.frame_int_now) + ' / ' + str(self.frame_max))
            # self.play_ret, self.frame_int_now = self.video_capture.read()
            # cv2.imshow(self.window_title, self.frame_int_now)
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# =============================================================================
class cv2_movie_player():
    logger = None
    window_size = None

    capture_frames : video_capture_frames = None
    namedWindow_value = None
    WindowProperty_values = None
    # info : movie_info = None
    window_title = ''
    # play_ret = None
    # frame_now = 0
    # frame_max = 0
    # video_capture = None
    # 動画の比率を保持する
    is_keep_movie_image_raito = True
    # state
    is_pause = True
    next_action = 0
    #
    few_rew_speed = const_play.FORWARD_REWIND_SPEED_DEFAULT.value
    # key
    control_keys : movie_player_key = movie_player_key()
    # file_name
    capture_file_name = const_play_str.CAPTURE_FILE_NAME_DEFAULT.value
    # =======================================
    def __init__(
            self, 
            logger_, 
            movie_path_:str,
            window_size,
            window_title='',
            movie_info_:cv2_movie_info=None) -> None:
        try:
            if cv2_movie_info == None:
                self.logger = logger_
                self.info = cv2_movie_info(logger_,movie_path_)
            else:
                self.info = movie_info_
                self.logger = movie_info_.logger
            self.window_title = window_title
            self.window_size = window_size
            self.capture_frames = video_capture_frames(self.info.logger,'',self.info)
        except Exception as e:
            logger_.exp.error(e)

    def initialize_before_show_window(
        self,namedWindow_value=None,WindowProperty_values = None) -> bool:
        try:
            # cv2.setings
            if namedWindow_value == None:
                namedWindow_value = \
                    const_play.CV2_NAMED_WINDOW_VALUE_DEFAULT_WINDOW_NORMAL               
            cv2.namedWindow(self.window_title,namedWindow_value)
            # cv2.settings
            if WindowProperty_values == None:
                WindowProperty_values = \
                    (const_play.CV2_WINDOW_PROPETY_VALUE1_WND_PROP_ASPECT_RATIO,
                    const_play.CV2_WINDOW_PROPETY_VALUE2_WINDOW_AUTOSIZE)
            #cv2.setWindowProperty(self.window_title,WindowProperty_values[0],WindowProperty_values[1])
            cv2.setWindowProperty(self.window_title,WindowProperty_values[0])
            cv2.setWindowProperty(self.window_title,WindowProperty_values[1])
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

 # xxxxxxxxxxxxxxxxxxxxxxx
    def initialize_value(self,window_title,window_size,namedWindow_value=None,WindowProperty_values = None) -> bool:
        try:
            # self.window_title = window_title
            # # cv2.setings
            # if namedWindow_value == None:
            #     namedWindow_value = cv2.WINDOW_NORMAL                
            # cv2.namedWindow(self.window_title,namedWindow_value)
            # # cv2.settings
            # if WindowProperty_values == None:
            #     WindowProperty_values = (cv2.WND_PROP_ASPECT_RATIO,cv2.WINDOW_AUTOSIZE)
            # cv2.setWindowProperty(self.window_title,WindowProperty_values[0],WindowProperty_values[1])

            self.window_size = window_size
            # get Capture
            # self.video_capture = cv2.VideoCapture(self.info.movie_path)
            # # read
            # self.play_ret, self.frame_capture_now = self.video_capture.read()
            # # set frame_max
            # self.frame_max = int(self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
            flag = self.capture_frames.initialize_value(self.window_title)
            if not flag : self.logger.error('capture_frames.initialize_value Failed')
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def play(self,is_do_play_initialize=False):
        try:
            if is_do_play_initialize:
                flag = self.play_initialize()
                if not flag:
                    self.logger.exp.error('play_initialize failed -> return')
                    return False
            self.is_pause = False
            flag = self.play_loop()
            if flag :
                self.logger.info('movie_play end success')
            else:
                self.logger.exp.error('movie play end error')
            return flag
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def play_window(self):
        try:
            cv2.imshow(self.window_title, self.capture_frames.frame_capture_now)
        except Exception as e:
            self.logger.exp.error(e)           

    def play_loop(self):
        try:
            self.logger.info('play_loop begin')
            while(self.capture_frames.video_capture.isOpened()):
                # Frame が最大(終了位置)でない、かつ、再生状態フラグ時に次を読み込む
                if not self.capture_frames.frame_is_over_max():
                    if not self.is_pause:
                        #self.play_ret,self.capture_frames.frame_capture_now = self.video_capture.read()
                        self.capture_frames.move_next()
                if self.capture_frames.play_ret:
                    # ウィンドウが不可視なら、再生をやめる
                    prop = cv2.getWindowProperty(self.window_title,cv2.WND_PROP_VISIBLE)
                    if not prop:
                        print('cv2.window visible False -> break')
                        break
                    # 読み込んだものを表示する
                    #cv2.imshow(self.window_title, self.capture_frames.frame_now)
                    self.play_window()
                    # Key入力を待つ
                    key_pushed = cv2.waitKey(20) & 0xFF
                    # Keyイベント処理
                    self.next_action = self.key_event(key_pushed)
                    # Next Action
                    if self.next_action == const_play.EXIT : break
                    elif self.next_action == const_play.ERROR:
                        self.logger.exp.error('self.next_action == const_play.ERROR continue')
                        self.next_action = const_play.NONE
                    # do process when end frame
                    self.process_end_frame_stop_when_end()
                ## end if :self.capture_frames.play_ret==True
            ## end Loop
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False
        finally:
            self.video_capture.release()
            cv2.destroyAllWindows()

    def process_end_frame_stop_when_end(self):
        try:
            if self.capture_frames.frame_is_max_or_max_over():
                if not self.is_pause:
                    # STOP する、再生中なら
                    self.is_pause = True
                    self.logger.info('frame >= frame_max -> pause')
        except Exception as e:
            self.logger.exp.error(e)

    def key_event(self,key_pushed):
        try:
            if key_pushed == ord(self.control_keys.exit):
                return const_play.EXIT
            elif key_pushed == ord(self.control_keys.pause_play) \
                or key_pushed == ord(self.control_keys.pause_play2):
                # 再生、一時停止フラグを切り替える
                self.play_pause_change()
            elif key_pushed == ord(self.control_keys.capture):
                # 現在表示されているイメージをファイルに保存する
                #self.capture_movie()
                self.capture_frames.capture_movie()
            elif key_pushed == ord(self.control_keys.previeous_frame_one):
                self.show_previous_frame_and_pause()
            elif key_pushed == ord(self.control_keys.next_frame_one):
                self.show_next_frame_and_pause()
            elif key_pushed == ord(self.control_keys.rewind):
                self.move_frame(-self.few_rew_speed)
            elif key_pushed == ord(self.control_keys.forward):
                self.move_frame(self.few_rew_speed)
            else:
                if key_pushed != 255:
                    self.logger('push_key = ' + str(key_pushed))
                    key_pushed = 255
            return const_play.NONE
        except Exception as e:
            self.logger.exp.error(e)
            return const_play.ERROR



    def show_next_frame_and_pause(self,move_frame_count=1):
        """次のフレームを表示する（実行時に一時停止となる）"""
        self.is_pause = True
        self.move_frame(move_frame_count)

    def show_previous_frame_and_pause(self,move_frame_count=-1):
        """前のフレームを表示する（実行時に一時停止となる）"""
        self.is_pause = True
        self.move_frame(move_frame_count)

    def move_frame(self,frame_count):
        try:
            self.capture_frames.move_frame(frame_count)
            self.play_window()
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    # xxxxxxxxxxxxxxxxxxxxx
    # def move_frame(self,move_frame_count=0):
    #     """任意の位置のフレームを表示する（実行時に一時停止となる）
    #     デフォルトは1フレーム進む
    #     """
    #     try:
    #         self.is_pause = True
    #         # 現在の再生位置（フレーム位置）の取得
    #         self.frame_now = int(self.video_capture.get(cv2.CAP_PROP_POS_FRAMES))
    #         # 最後の位置より上、ゼロより下の場合は処理を中断する
    #         if self.frame_now + move_frame_count > self.frame_max \
    #             or self.frame_now + move_frame_count < 0:
    #             self.logger.info('[frame_now + move_frame_count] == [> frame_max] or [< 0]')
    #             return
            
    #         # 以下 read 時に1フレーム進むので、-1 する
    #         self.frame_now += move_frame_count -1
    #         # frame をセットして読み込み、表示する
    #         self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, self.frame_now)
    #         print('frame_now = ' + str(self.frame_now) + ' / ' + str(self.frame_max))
    #         self.play_ret, self.frame_now = self.video_capture.read()
    #         cv2.imshow(self.window_title, self.frame_now)
            
    #     except Exception as e:
    #         self.logger.exp.error(e)

    # xxxxxxxxxxxxxxxxxxxxx
    # def capture_movie(self):
    #     # 現在表示されているイメージをファイルに保存する
    #     try:
    #         write_path = self.capture_file_name 
    #         cv2.imwrite(write_path,self.frame_now)
    #         self.logger.info('capture success. path= ' + write_path)
    #     except Exception as e:
    #         self.logger.exp.error(e)


    def play_pause_change(self):
        try:
            # 再生、一時停止フラグを切り替える
            self.is_pause = not self.is_pause
            if self.is_pause:
                self.logger.info('pause')
            else: 
                self.logger.info('play')
                if self.capture_frames.frame_is_max_or_max_over():
                    # 始点から再生、終点で停止中から再生なら
                    self.logger.info('frame_now >= frame_max -> play from frame 0')
                    #self.capture_frames.move_frame(0)
                    self.move_frame(-self.capture_frames.frame_int_now)
                    self.is_pause = False
                    # self.frame_now = 0
                    # self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, self.frame_now)
                    # self.play_ret, self.frame_now = self.video_capture.read()
                    # cv2.imshow(self.window_title, self.capture_frames.frame_now)
                    # self.play_window()
        except Exception as e:
            self.logger.exp.error(e)
    
    def play_initialize(self):
        try:
            self.capture_frames.initialize_value(self.window_title)
            # set window property
            self.initialize_before_show_window()
            # show window
            self.play_window()
            # set setting after show window
            # set window size
            self.set_window_size(self.window_size)
            new_size = (0,0)
            if self.is_keep_movie_image_raito:
                new_size = resize_to_fit_when_lager_than_new_size(
                    (self.capture_frames.frame_capture_now.shape[1],
                    self.capture_frames.frame_capture_now.shape[0]),
                    self.window_size)
                self.logger.info('resizeWindow = ' + str(new_size))
            if new_size != (0,0):
                cv2.resizeWindow(self.window_title,new_size[0],new_size[1])
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def set_window_title(self,window_title=''):
        try:
            if window_title == '':
                self.window_title = const_play_str.WINDOW_TITLE_DEFAULT.value
            else:
                self.window_title = window_title
            
            self.logger.info('movie_player.window_title = '+ self.window_title)
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def set_window_size(self,window_size):
        try:
            if window_size == (0,0):
                self.window_size = \
                    (int(self.capture_frames.frame_now.shape[1]),
                    int(self.capture_frames.frame_now.shape[0]))
            else:
                self.window_size = window_size
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

# =============================================================================
# common method (not class)
# new size より大きいときフィットするようリサイズする
# Resize to fit when larger than new size
def resize_to_fit_when_lager_than_new_size(frame_size,new_size):
    try:
        new_width = new_size[0]
        new_height = new_size[1]
        frame_width = frame_size[0]
        frame_height = frame_size[1]
        # new_size がゼロの場合は何もしない
        if (new_width <= 0) or (new_height <= 0):
            return frame_size
        # new_size より小さい場合は何もしない
        if (frame_width >= new_width) and (frame_height >= new_height):
            return frame_size
        # 縦横それぞれの比率を求める
        width_raito = frame_width / new_width
        height_raito = frame_height / new_height
        # 比率が大きいほうに合わせる
        if width_raito > height_raito:
            new_raito = width_raito
        else:
            # width_raito <= height_raito
            new_raito = height_raito
        
        ret_width = int(frame_width / new_raito)
        ret_height = int(frame_height / new_raito)
        return ret_width,ret_height
    except:
        import traceback
        print(traceback.print_exc())
        return frame_size

class VideoCaptureFrames(video_capture_frames):
    pass