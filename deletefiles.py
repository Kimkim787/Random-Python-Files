import os
import shutil

path = "C:\\Python\\basics\\deltefile.txt"
dir = "C:\\Python\\basics\\delte_folder"

try:
    # os.remove(path) # remove files
    # os.rmdir(dir) # remove empty directories
    shutil.rmtree(dir) # remove directories and everything in it (considered dangerous)
except FileNotFoundError:
    print("File not found")
except PermissionError:
      print("Permission Denied!")
except OSError:
    print("Cannot delete Folder with Files")
else: 
    print("File deleted!")
finally:
    print("End of program")