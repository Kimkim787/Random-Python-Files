import os

path = "C:\\Users\\alcan\\OneDrive\\Documents\\sad.txt" #any file

if os.path.exists(path):
    print("path exist")
    if os.path.isfile(path):
        print("It is a File")
    elif os.path.isdir(path):
        print("It is a Directory") 
else:
    print("path doesn't exist")

print("------------ second section ------------")
path = "C:\\Users\\alcan\\OneDrive\\Documents\\Zoom" #any folder
if os.path.exists(path):
    print("path exist")
    if os.path.isfile(path):
        print("It is a File")
    elif os.path.isdir(path):
        print("It is a Directory")
else:
    print("path doesn't exist")