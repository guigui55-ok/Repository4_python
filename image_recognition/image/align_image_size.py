
import sys
from pathlib import Path
path = Path(__file__).parent.parent
print('sys.path.append = {}'.format(path))
sys.path.append(str(path))

from ir_preapare_test1 import get_target_dir_path
from ir_preapare_test1 import get_image_path_list

from ir_test1 import Cv2Image, ImageDataCreater

def main():
    target_path = get_target_dir_path()
    paths = get_image_path_list(target_path)
    list_creater = ImageDataCreater()
    # limit = -1 #No limit
    limit = 100
    image_list = list_creater.set_image_from_paths(paths, limit)
    for image_obj in list_creater.image_obj_list:
        buf = image_obj.get_aspect_ratio_str()
        print(buf)

if __name__ == '__main__':
    print('')
    print('*****')
    main()

