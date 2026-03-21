f = open("0009 File Input-Output/myfile.txt")

# lines = f.readlines()
# line1 = f.readlines()
# print(line1, type(line1))

# line2 = f.readlines()
# print(line2, type(line2))
# f.close()

# using while loop

line = f.readline()

while line != "":
    print(line)
    line = f.readline()

f.close()