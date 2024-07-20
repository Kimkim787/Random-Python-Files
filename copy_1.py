# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata ( file's creation and modification times)

import shutil as copy

copy.copyfile( ".\\text.txt", ".\\copiedfiles\\copyfile.txt") # parameters are ( src, destination )
copy.copy(".\\text.txt", ".\\copiedfiles")