# 7. Write a program to find out the line number where python is present from ques 6

with open("0009 File Input-Output/Practice Set/log.txt") as f:
    lines = f.readlines()

lineno = 1

for line in lines:
    if "python" in line:
        print(f"python is present. Line no. {line}")
        break
    lineno += 1

else:
    print("python is not present.")