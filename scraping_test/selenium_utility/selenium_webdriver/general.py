

if __name__ == '__main__':
    import selenium_const
else:
    import selenium_webdriver.selenium_const as selenium_const
import time

class Waiter():
    def __init__(self,defalut_wait_time:float=selenium_const.DEFAULT_WAIT_TIME) -> None:
        self.defalut_wait_time = defalut_wait_time
        self.is_logout = False
    
    def wait(self,wait_time:float=-1):
        wait_time = self.__get_wait_time(wait_time)
        if self.is_logout:
            print('Wait Start. {} sec. '.format(wait_time),end='')
        time.sleep(wait_time)
        if self.is_logout:
            print('End.')
    
    def __get_wait_time(self,wait_time:float=-1):
        if wait_time < 0:
            wait_time = self.defalut_wait_time
        return wait_time
    def wait_little(self,wait_time:float=-1):
        wait_time = self.__get_wait_time(wait_time) /5
    def wait_short(self,wait_time:float=-1):
        wait_time = self.__get_wait_time(wait_time) /2
    def wait_long(self,wait_time:float=-1):
        wait_time = self.__get_wait_time(wait_time) *2
    def wait_longer(self,wait_time:float=-1):
        wait_time = self.__get_wait_time(wait_time) *5
    def wait_longest(self,wait_time:float=-1):
        wait_time = self.__get_wait_time(wait_time) *10
    def wait_half_minute(self):
        self.wait(30)
