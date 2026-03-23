f = open("0009 File Input-Output/myfile.txt")

print(f.read())

f.close()

# The same can be written using with statement lite this:-

with open("0009 File Input-Output/myfile.txt") as f:
    print(f.read())

# Don't have to explicitly close the file