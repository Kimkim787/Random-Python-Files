try:
    with open("C:\\Python\\basics\\text.txt") as file:
        print("The File exists")
        print(file.read())
        print("Inside WITH block: ",file.closed)
except Exception:
    print("File not Found")

print("Outside WITH block: ",file.closed)