# 6. Write a program to mine a log file and find out whether it contains ‘python’.

with open("0009 File Input-Output/Practice Set/log.txt") as f:
    content = f.read()

if "python" in content:
    print("python is present.")
else:
    print("python is not present.")