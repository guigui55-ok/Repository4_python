
from distutils.debug import DEBUG
from http.server import ThreadingHTTPServer
from cv2 import threshold
import import_init
DEBUG_TRACE = 1
DEBUG_DEBUG = 2
DEBUG_MODE = DEBUG_DEBUG
NEW_LINE = '\n'

def main():
    target_path = r'F:\ZPICTURE\jpg ss new\jpg New\0jpg op base image\op new__________new2\220501'
    target_path = r'C:\Users\OK\source\repos\Repository4_python\comp_pic\image'
    comp_path = target_path
    jpg_path_list = get_file_path_list(target_path,'jpg')
    excute_comp_pic(jpg_path_list)
    return

def excute_comp_pic(path_list:'list[str]'):
    debug_print()
    debug_print('===========')
    for base_path in path_list:
        #read file
        base_cv2img = read_image(base_path)
        debug_print('base_path = ')
        debug_print(base_path)
        for comp_path in path_list:
            debug_print('.',end='')
            if base_path == comp_path:
                pass
                debug_print('/',end='')
            else:
                #comp read file
                comp_cv2img = read_image(comp_path)

                # is_match = cv2_image_comp.is_same_image(None,base_cv2img.img,comp_cv2img.img)
                threshold = 0.5
                comp_val = cv2_image_comp.get_compareist_value(None,base_cv2img.img,comp_cv2img.img)
                if comp_val >= threshold:
                    debug_print()
                    print('    [{}]'.format(comp_val))
                    print('{}'.format(comp_path))

        debug_print()
        print('***** test break')
        break

import common_utility.cv2_image.cv2_image_comp as cv2_image_comp
import common_utility.cv2_image.cv2_image_util as cv2_image_util
def read_image(path):
    cv2img = cv2_image_util.Cv2Image(path)
    return cv2img

def get_file_path_list(path:str,ext:str):
    import glob
    value = path + '/*.' + ext
    file_list = glob.glob(value)
    if DEBUG_MODE < DEBUG_DEBUG:
        print()
        print('----------')
        for file in file_list:
            print('  ' + file)
    return file_list

def debug_print(value='',end=None):

    if DEBUG_MODE >= DEBUG_TRACE:
        if end == None:
            print(value)
        else:
            print(value,end=end)

if __name__ == '__main__':
    main()