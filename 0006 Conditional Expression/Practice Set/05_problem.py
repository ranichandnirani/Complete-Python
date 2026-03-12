# 5. Write a program which finds out whether a given name is present in a list or not.

li = ["Chandni", "Khushi", "Satinder", "Gauri"]

name = input("Enter your name: ")
if(name in li):
    print("Your name is in the list.")

else:
    print("Your name is not in the list.")