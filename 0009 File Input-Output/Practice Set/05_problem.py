# 5. Repeat program 4 for a list of such words to be censored.

words = ["Donkey", "Bad", "Ganda"]

with open("0009 File Input-Output/Practice Set/donkey.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word)) 

with open("0009 File Input-Output/Practice Set/donkey.txt","w") as f:
    f.write(content)