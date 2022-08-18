import os 
print("Current folder")
print(os.getcwd())
print(os.listdir())
print("c drive content")
os.chdir('C:\\')
print(os.getcwd())
print(os.listdir())

address=r'C:\Users\Yash\Documents\certificates'
if os.path.exists(address):
    print('file exist')
else:
    print("file not exist")