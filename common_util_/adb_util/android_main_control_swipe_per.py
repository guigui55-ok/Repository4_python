

# from common_util.adb_util import device_info
# from common_util.adb_util.adb_common import is_success_adb_result, screen_capture_for_android


from common_util.adb_util.adb_common import excute_command
from common_util.adb_util.android_main_control_swipe import AndroidControlSwipe



if __name__ == '__main__' or __name__ == 'android_main_control':
    import adb_key  
    from  device_info import DeviceInfo
    import adb_common
    from android_const import Constants
    from android_control_cv2_image import AndroidControlCv2Image
    from android_control_cv2_movie import AndroidControlCv2Movie
    from android_control_adb import AndroidControlAdb
    from android_main_control_swipe import AndroidControlSwipe
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
    from common_util.adb_util.android_main_control_swipe import AndroidControlSwipe
    from common_util.general_util.rectangle import RectAngle

class AndroidControlSwipePer(AndroidControlSwipe):
    def __init__(self, logger, control:AndroidControlAdb, img_path='') -> None:
        super().__init__(logger, control, img_path)
    
    def swipe(self, x1, y1, x2, y2, duration) -> bool:        
        x1,y1,x2,y2 = self.cnv_location_from_percent(x1,y1,x2,y2)
        return super().swipe(x1, y1, x2, y2, duration)
    
    def up(self, x, y1, y2, duration) -> bool:
        x1,y1,x2,y2 = self.cnv_location_from_percent(x,y1,x,y2)
        return super().up(x1, y1, y2, duration)
    
    def up_fast(self, x, y1, y2) -> bool:
        x1,y1,x2,y2 = self.cnv_location_from_percent(x,y1,x,y2)
        return super().up_fast(x1, y1, y2)
    
    def down(self, x, y1, y2, duration=...) -> bool:
        x1,y1,x2,y2 = self.cnv_location_from_percent(x,y1,x,y2)
        return super().down(x1, y1, y2, duration=duration)
    
    def down_fast(self, x, y1, y2) -> bool:
        x,y1,x2,y2 = self.cnv_location_from_percent(x,y1,x,y2)
        return super().down_fast(x, y1, y2)

    def by_rect(self, rect: RectAngle, duration: int) -> bool:
        rect_cnv = self.cnv_location_from_percent_for_rect(rect)
        return super().by_rect(rect_cnv, duration)   

    def up_fast_x_center(self, y1, y2=None):
        x1,y1,x2,y2 = self.cnv_location_from_percent(0,y1,0,y2)
        return super().up_fast_x_center(y1, y2=y2)
    
    def down_fast_x_center(self, y1, y2=None):
        x1,y1,x2,y2 = self.cnv_location_from_percent(0,y1,0,y2)
        return super().down_fast_x_center(y1, y2=y2)