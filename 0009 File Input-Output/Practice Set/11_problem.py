# 11. Write a python program to rename a file to “renamed_by_ python.txt

with open("0009 File Input-Output/Practice Set/old.txt") as f:
    content = f.read()

with open("0009 File Input-Output/Practice Set/rename_by_python.txt", "w") as f:
    f.write(content)