from typing import Any
import cv2
import os

from common_utility.cv2_image.import_logger import log_info,log_error,LoggerUtility

class Cv2ImageObject():
    main=None
    def __init__(self) -> None:
        pass

class Cv2Image():
    """イメージの読み書き、リサイズ、大きさ比較など基本的な機能を持つクラス"""
    path = ''
    logger = None
    img = None
    def __init__(self,pathOrCv2Image:Any = '',cv2_method:int=-1) -> None:
        """
        引数：
        pathOrCv2Image：イメージの path か、cv2.imread ですでに取得しているイメージを渡す"""
        path = ''
        if type(pathOrCv2Image) is str:
            path = str(pathOrCv2Image)
            self.path = path
            if path == '' : 
                return            
            is_set = self.set_image_from_path(path,cv2_method)
        else:
            is_set = self.set_image(pathOrCv2Image)
        if not is_set:
            log_error(__name__ +'.__init__ :set image ERROR')
    
    def get_image_from_path(self,path:str ='',cv2_method:int=-1)-> Any:
        """path の存在チェック、存在するときはメンバへ格納し、
        イメージを読み込み、イメージオブジェクトを返す
        """
        self.path = path
        if not os.path.exists(self.path):
            log_error(__name__ + ':path not exists. path=' + self.path)
            return None
        if cv2_method < 0:
            img = cv2.imread(path)
        else:
            img = cv2.imread(path,cv2_method)
        return img

    def set_image(self,img:Any) -> bool:
        if self.object_is_cv2image(img):
            self.img = img
        else:
            log_error('cv2_image.set_image: img type is not cv2image')
            return False
        return True
    
    def object_is_cv2image(self,value)->bool:
        try:
            # cv2image 固有のプロパティにアクセスしてエラー出ないか判定する
            buf = value.shape
            return True
        except:
            return False

    def set_image_from_path(self,path:str,cv2_method:int=-1) -> bool:        
        """path の存在チェック、存在するときはメンバへ格納し、
        イメージを読み込み、イメージオブジェクトをメンバ変数へ格納する"""
        try:
            img = self.get_image_from_path(path,cv2_method)
            if len(img) <= 0:
                return False
            self.img = img
            return True
        except Exception as e:
            log_error(e)
            return False

    def resize(self,width:int,height:int) -> bool:
        """イメージをリサイズする"""
        # if self.is_image_none('resize'): return False
        self.img = cv2.resize(self.img,dsize=(width,height))
        log_info('resized : w='+ str(self.img.shape[1]) + ' ,h=' + str(self.img.shape[0]))
    
    def resize_by_image(self,arg_img):
        """メンバ self.img を引数 arg_img の大きさにする"""
        self.resize(arg_img.shape[1],arg_img.shape[0])

    def is_image_none(self,func_name = '') -> bool:
        """イメージが None であるか判定する"""
        try:
            if self.img is None:
                if func_name != '':
                    func_name = '.'+func_name
                log_error(__name__ + func_name + ':self.img is None')
                return True
            return False
        except Exception as e:
            log_error(e)
            return True
    
    def save_img_with_name_auto(self,add_name:str='',dir:str='.'):
        """イメージを save_path に出力する。名前を自動的に指定
            name = add_name_%y%m_%H%M%S.png
        """
        import datetime
        if add_name != '' : add_name += '_'
        name = add_name
        name += datetime.datetime.now().strftime('%y%m_%H%M%S')
        name += '.png'
        import os
        path = os.path.join(dir,name)
        self.save_img_other(path,self.img)
        return path

    def save_img_other(self,save_path:str,save_img,logout=False)->bool:
        """イメージを save_path に出力する"""
        if os.path.exists(save_path):
            log_error(__name__ + '.save_img:save_path is already exists. path=' + save_path)
            log_error('save_img Failed: not saved , return')
            return False
        cv2.imwrite(save_path,save_img)
        if logout:
            log_info('save_img: save_path = ' + save_path)
        return True
    
    def save_img(self,save_path:str)->bool:
        """イメージを save_path に出力する"""
        self.save_img(save_path,self.img)
    
    def width(self) -> int:
        """イメージの幅を取得する"""
        # if self.is_image_none('width'): return 0
        return self.img.shape[1]
    
    def height(self) -> int:
        """イメージの高さを取得する"""
        # if self.is_image_none('height'): return 0
        return self.img.shape[0]


    def is_big_self_image(self,arg_img):
        """self.img のサイズが arg_img のサイズより大きいか判定する"""
        # 両方大きい
        if ((self.width() > arg_img.shape[1]) and
            (self.height() > arg_img.shape[0])):
            return True
            
        # self_size = self.width() + self.height()
        # arg_size = arg_img.shape[1] + arg_img.shape[0]
        # if self_size >= arg_size:
        #     return True
        # else:
        #     return False

    def resize_keep_raito(self,raito)->bool:
        """縦横比を維持したまま、リサイズする
        raito : 倍率"""
        h , w = self.img.shape[:-1]
        self.img = cv2.resize(self.img,(int(w * raito),int(h * raito)))
    
    def triming(self,rect):
        """画像をトリミング（切り抜き）する
        rect = [ begin.x , begin.y , end.x , end.y ]
        """
        img_tri = self.img[rect[1] : rect[3], rect[0] : rect[2]]
        # img_tri = self.img[rect[0] : rect[2], rect[1] : rect[3]]
        return img_tri
