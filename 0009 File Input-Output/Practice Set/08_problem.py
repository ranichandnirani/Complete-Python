# 8. Write a program to make a copy of a text file “this. txt”

with open("0009 File Input-Output/Practice Set/this.txt") as f:
    content = f.read()

with open("0009 File Input-Output/Practice Set/this_copy.txt", "w") as f:
    f.write(content)   