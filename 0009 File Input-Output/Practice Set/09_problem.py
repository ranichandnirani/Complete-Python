# 9. Write a program to find out whether a file is identical & matches the content of another file.

with open("0009 File Input-Output/Practice Set/this.txt") as f:
    content1 = f.read()

with open("0009 File Input-Output/Practice Set/poem.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("This file is identical")
else:
    print("Not identical")