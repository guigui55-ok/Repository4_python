

# from common_util.adb_util import device_info
# from common_util.adb_util.adb_common import is_success_adb_result, screen_capture_for_android


if __name__ == '__main__' or __name__ == 'android_main_control':
    import adb_key  
    from  device_info import DeviceInfo
    import adb_common
    from android_const import Constants
    from android_control_cv2_image import AndroidControlCv2Image
    from android_control_cv2_movie import AndroidControlCv2Movie
    from android_control_adb import AndroidControlAdb
    from common_util.general_util.rectangle import RectAngle
else:
    # 外部から参照時は、common_util を sys.path へ追加しておくこと
    import common_util.adb_util.adb_key  
    from common_util.adb_util.device_info import DeviceInfo
    import common_util.adb_util.adb_common as adb_common
    from common_util.adb_util.android_const import Constants
    from common_util.adb_util.android_control_cv2_image import AndroidControlCv2Image
    from common_util.adb_util.android_control_cv2_movie import AndroidControlCv2Movie
    from common_util.adb_util.android_control_adb import AndroidControlAdb
    from common_util.general_util.rectangle import RectAngle

class AndroidControlSwipe():
    logger = None
    const : Constants= None
    control_cv2_img:AndroidControlCv2Image
    control_cv2_mov:AndroidControlCv2Movie
    control_adb:AndroidControlAdb
    device_info : DeviceInfo
    ocr_control = None
    control_mode = 1
    def __init__(self,logger,control:AndroidControlAdb,img_path='') -> None:
        self.logger = logger
        self.device_info = control.device_info
        self.const = Constants
        self.control_mode = self.const.main.CONTROL_MODE_IMG_CV2.value
        self.control_adb = control

        self.const_screen_image_file_names = self.const.image_file
    
    def swipe(self,x1,y1,x2,y2,duration)->bool:
        """ swipe basic method """
        # CONTROL_MODE_ADB only
        flag,ret =self.control_adb.swipe(x1,y1,x2,y2,duration)
        return flag
    
    def by_rect(self,rect:RectAngle,duration:int)->bool:
        return self.swipe(
            rect.begin.x,rect.begin.y,
            rect.end.x,rect.end.y,duration
        )

    def list_to_rectAngle(self,list_for_swipe):
        """[100,110,200,210,500] -> Rectangle , duration"""
        try:
            rect = RectAngle()
            rect.set_value_by_list(list_for_swipe)
            duration = list_for_swipe[4]
            return rect , duration
        except Exception as e:
            self.logger.exp.error(e)
            return RectAngle(),0
    
    def by_percent(self,x1_per,y1_per,x2_per,y2_per,duration)->bool:
        try:
            ratio = 0.01
            x1 = self.device_info.width * ratio * x1_per
            y1 = self.device_info.height * ratio * y1_per
            x2 = self.device_info.width * ratio * x2_per
            y2 = self.device_info.height * ratio * y2_per
            return self.swipe(x1,y2,x2,y2,duration)
        except Exception as e:
            self.logger.exp.error(e)
            return False
    
    def cnv_location_from_percent(self,x1_per,y1_per,x2_per,y2_per):
        try:
            ratio = 0.01
            x1 = self.device_info.width * ratio * x1_per
            y1 = self.device_info.height * ratio * y1_per
            x2 = self.device_info.width * ratio * x2_per
            y2 = self.device_info.height * ratio * y2_per
            return x1,y1,x2,y2
        except Exception as e:
            self.logger.exp.error(e)
            return []
    
    def cnv_location_from_percent_for_rect(self,value_per:RectAngle):
        loc_rect = RectAngle()
        try:
            ratio = 0.01
            w = self.device_info.width
            h = self.device_info.height
            loc_rect.begin.x = w * value_per.begin.x * ratio
            loc_rect.begin.y = h * value_per.begin.y * ratio
            loc_rect.end.x = w * value_per.end.x * ratio
            loc_rect.end.y = h * value_per.end.y * ratio
            return loc_rect
        except Exception as e:
            self.logger.exp.error(e)
            return loc_rect

    def up(self,x,y1,y2,duration)->bool:
        """ scroll_down """
        try:
            x1 = x
            x2 = x
            y1,y2 = self.swap_values(y1,y2)
            return self.swipe(x1,y1,x2,y2,duration)
        except Exception as e:
            self.logger.exp.error(e)
            return False
    
    def up_fast(self,x,y1,y2)->bool:
        """ scroll_down """
        duration = Constants.main.SWIPE_FAST_DURATION.value
        return self.swipe_up(x,y1,y2,duration)
    
    def down(
    self,x,y1,y2,
    duration = Constants.main.SWIPE_NORMAL_SPEED.value)->bool:
        """ scroll_up """
        try:
            x1 = x
            x2 = x            
            y1 , y2 = self.swap_values(y1,y2)
            return self.swipe(x1,y1,x2,y2,duration)
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def swap_values(self,value1:int,value2:int,order=Constants.main.ORDER_ASCENDING):
        """値を入れ替える。orderで昇順・降順を指定する
        order 規定値は昇順"""
        try:
            if order == Constants.main.ORDER_ASCENDING:
                if value1 > value2:
                    return value2,value1
                else:
                    return value1,value2
            elif order == Constants.main.ORDER_DEASCENDING:
                if value1 > value2:
                    return value1,value2
                else:
                    return value2,value1
            else:
                self.logger.exp.error('order is invalid')
                return value1,value2

        except Exception as e:
            self.logger.exp.error(e)
            return value1,value2

    def down_fast(self,x,y1,y2)->bool:
        """ scroll_up """
        duration = Constants.main.SWIPE_FAST_DURATION.value
        return self.swipe_down(x,y1,y2,duration)

    def up_fast_x_center(self,y1,y2=None):
        """ scroll_down """
        try:
            if y2 == None:
                y2 = self.device_info.height * 0.1
            if y1 > y2:
                y2 = int(y1/10)
                self.logger.exp.error('y1 > y2 , y2 = int(y1/10) ,continue')
            x = int(self.device_info.width /2)
            return self.swipe_down_fast(x,y1,y2)
        except Exception as e:
            self.logger.exp.error(e)
            return False
        
    def down_fast_x_center(self,y1,y2=None):
        """ scroll_up """
        try:
            if y2 == None:
                y2 = self.device_info.height * 0.9
            if y1 > y2:
                y2 = int(y1/10)
                self.logger.exp.error('y1 > y2 , y2 = int(y1/10) ,continue')
            x = int(self.device_info.width /2)
            return self.swipe_down_fast(x,y1,y2)
        except Exception as e:
            self.logger.exp.error(e)
            return False