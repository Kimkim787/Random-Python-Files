import os

source = "copiedfiles" # files or directories
destination = "C:\\Python\\basics\\moved" # moved folder must not exists. the code can create it automaticaly

try:
    if os.path.exists(destination):
        print("Folder already exists")
    else:
        os.replace(source, destination)
        print(source, " is moved")
except FileNotFoundError as err:
    print(source, "not found")