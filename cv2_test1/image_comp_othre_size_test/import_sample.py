
import traceback
import import_init

def get_paths():
    try:
        import pathlib,os
        dir_path = str(pathlib.Path(__file__).parent.parent)
        image_path = os.path.join(dir_path,'image','histgram')
        file_base = 'sample.png'
        base_path = os.path.join(image_path,file_base)
        if not os.path.exists(base_path):
            print('not exists : ' + base_path)
        return dir_path,base_path
    except:
        traceback.print_exc()

def main():
    try:        
        logger = import_init.initialize_logger_new()

        return
    except:
        traceback.print_exc()