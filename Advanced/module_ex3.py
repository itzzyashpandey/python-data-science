import os 
print("Current folder")
print(os.getcwd()) #place where code run 
print(os.listdir()) #files in cwd
print("c drive content")
os.chdir('C:\\') #place where we want to run code 
print(os.getcwd())
print(os.listdir())

address=r'C:\Users\Yash\Documents\certificates'
if os.path.exists(address):
    print('file exist')
else:
    print("file not exist")