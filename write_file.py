w = "This will overwrite the text file. From write_file.py"
a = "Text appended from write_file.py"
try:
    with open("C:\\Python\\basics\\text.txt", "w") as file: # "w" overwrites a file
        file.write(w + "\n")
except Exception:
    print("File not found")

try:
    with open("C:\\Python\\basics\\text.txt", "a") as file: # "a" append the text to the file
        file.write(a)
except Exception:
    print("File not found")
