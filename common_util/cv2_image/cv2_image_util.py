from typing import Any
import cv2
import os

class cv2_image():
    path = ''
    logger = None
    img = None
    def __init__(self,logger,path:str = '') -> None:
        self.path = path
        self.logger = logger
        if path == '' : 
            return            
        is_set = self.set_image_from_path(path)
        if not is_set:
            self.logger.warning(__name__ +'.__init__ :set image ERROR')
    
    def get_image_from_path(self,path ='')-> Any:
        fn = '.get_image_from_path'
        try:
            if(path == '')|(path == None):
                self.logger.exp.error(__name__ + fn +':path is nothing')
                return None
            else:
                self.path = path
                if not os.path.exists(self.path):
                    self.logger.exp.error(__name__ + fn +':path not exists. path=' + self.path)
                    return None

            img = cv2.imread(path)
            return img
        except Exception as e:
            self.logger.exp.error(e)
            return None


    def set_image_from_path(self,path = path) -> bool:
        fn = '.set_image_from_path'
        try:
            img = self.get_image_from_path(path)
            if len(img) <= 0:
                return False
            self.img = img
            self.logger.info(fn + ' success. path = '+ path)
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def resize(self,width:int,height:int) -> bool:
        if self.is_image_none('resize'): return False
        try:
            self.img = cv2.resize(self.img,dsize=(width,height))
            self.logger.info('resized : w='+ str(self.img.shape[1]) + ' ,h=' + str(self.img.shape[0]))
        except Exception as e:
            self.logger.exp.error(e)
    
    def resize_by_image(self,arg_img):
        try:
            self.resize(arg_img.shape[1],arg_img.shape[0])
        except Exception as e:
            self.logger.exp.error(e)

    def is_image_none(self,func_name = '') -> bool:
        try:
            if self.img is None:
                if func_name != '':
                    func_name = '.'+func_name
                self.logger.exp.error(__name__ + func_name + ':self.img is None')
                return True
            return False
        except Exception as e:
            self.logger.exp.error(e)
            return True
    
    def save_img(self,save_path:str):
        try:
            if not os.path.exists(self.path):
                self.logger.error(__name__ + '.save_img:save_path not exists. path=' + save_path)
            cv2.imwrite(save_path,self.img)
            self.logger.info('save_img: save_path = ' + save_path)
        except Exception as e:
            self.logger.exp.error(e)
    
    def width(self) -> int:
        try:
            if self.is_image_none('width'): return 0
            return self.img.shape[1]
        except Exception as e:
            self.logger.exp.error(e)
    def height(self) -> int:
        try:
            if self.is_image_none('height'): return 0
            return self.img.shape[0]
        except Exception as e:
            self.logger.exp.error(e)


    def is_big_self_image(self,arg_img):
        try:
            # 両方大きい
            if ((self.width() > arg_img.shape[1]) and
                (self.height() > arg_img.shape[0])):
                return True
                
            self_size = self.width() + self.height()
            arg_size = arg_img.shape[1] + arg_img.shape[0]
            if self_size >= arg_size:
                return True
            else:
                return False
        except Exception as e:
            self.logger.exp.error(e)