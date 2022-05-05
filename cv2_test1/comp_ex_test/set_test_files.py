

import shutil,os,pathlib

dir_parent = str(pathlib.Path(__file__).parent)
dist_dir_name = 'image'
dist_dir = os.path.join(dir_parent,dist_dir_name)
src_dir_name = 'image_base'
src_dir = os.path.join(dir_parent,src_dir_name)

#Pythonでファイルを削除するにはos.remove()、
# ディレクトリ（フォルダ）を中のファイルやサブディレクトリごとすべて削除するには
# shutil.rmtree()を使う
if os.path.exists(dist_dir):
    # os.remove(dist_dir)
    shutil.rmtree(dist_dir)
# shutil.copy(src_dir,dist_dir)
shutil.copytree(src_dir,dist_dir)

#delete files in dir
delete_dir_name = 'comp_dir'
delete_dir = os.path.join(dir_parent,delete_dir_name)
import glob
path_list = glob.glob(delete_dir + '/*.png')
for path in path_list:
    if not os.path.isdir(path):
        os.remove(path)

