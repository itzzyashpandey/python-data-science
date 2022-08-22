from genericpath import isfile
import os
from datetime import datetime

#create Folder 
if os.path.exists('test'):
    print("test folder exist")
else:
    os.mkdir("test")
    print("test folder created")


#create multi level folder 
folder= 'a/b/c/d/e/f/g'
if os.path.exists(folder):
    print("path exists")
else :
    os.makedirs(folder)
    print("path created")


#delete a file  
if os.path.exists('faltu'):
    os.unlink('faltu')
    print('faltu deleted')
else:
    print("faltu not exist")
    
#delete a folder
if os.path.exists('test'):
    os.rmdir('test')
    print('test deleted')
else:
    print("test not exist")
    
#display file details
if os.path.exists('basics/hello.py'):
    size=os.path.getsize('basics/hello.py')
    ctime=os.path.getctime('basics/hello.py')
    mtime=os.path.getmtime('basics/hello.py')
    isfile =os.path.isfile('basics/hello.py')
    
    isdir = os.path.isdir('basics/hello.py')
    print("filename:  basics/hello.py")
    
    print("size:", size,'bytes')
    print("ctime", datetime.fromtimestamp(ctime))
    print("mtime", datetime.fromtimestamp(mtime))
    print("isfile:", isfile)
    print("isdir:", isdir)
    
    
#recursive display file tree
for root , dirs, files in os.walk('.'):
    print(f"folder is {root.upper()}")
    print("total folders:", len(dirs))
    print("files in this folder are:", files)
    
