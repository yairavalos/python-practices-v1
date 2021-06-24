# Create a package named as you
# Create a module for json handling
# Create a module for math basis ops

import os

split_dir = os.path.split(os.getcwd())
split_dir

join_dir = os.path.join(str(split_dir[0]),str(split_dir[1]))
join_dir

mydir_list = os.listdir(os.getcwd())
mydir_list
mydir_list[0]

myattr = os.listxattr(os.getcwd())
myattr

myscan_dir = os.scandir(os.getcwd()) 
type(myscan_dir)
myscan_dir.__str__()
[print(item) for item in myscan_dir]
myscan_dir.__dict__


from pathlib import Path

p = Path('./PythonG2')
mypath_list = [x for x in p.iterdir()]
mypath_list

mypath_list[0].is_dir()
mypath_list[2].is_dir()
mypath_subtree_list = [file for file in mypath_list[2].iterdir()]
[print(f'Dir: {item}') for item in mypath_subtree_list if item.is_dir()] 
[print(f'File: {item}') for item in mypath_subtree_list if item.is_file()]


mypath_list[0].is_file()
mypath_list[0].absolute()
myresult = mypath_list[0].glob('./scripts')
myresult_list = [item for item in myresult]
myresult_list

from yair_pkg.my_json import myJSON

jsonHandler = myJSON()
jsonHandler.read_my_json("Test")

