# 4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file. .

word = "Donkey"

with open("0009 File Input-Output/Practice Set/donkey.txt","r") as f:
    content = f.read()

content = content.replace("Donkey", "#####") 

with open("0009 File Input-Output/Practice Set/donkey.txt","w") as f:
    f.write(content)