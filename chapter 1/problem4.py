# wap to print the contents of a diectory using the os module
# search online for the function which does that 

import os

# specify directory path (you can change this)
path = "/ new folder"

# get directory contents
files = os.listdir(path)

# print each file/folder
for file in files:
    print(file)