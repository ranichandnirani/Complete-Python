# write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

# specify the path of the directory
directory_path = "/chandni/Python"

# get list of contents
contents = os.listdir(directory_path)

# print each item
for item in contents:
    print(item)
