# 2. Write a python program using function to convert Celsius to Fahrenheit

# c/5 = (f-32)/9

f = int(input("Enter the temprature in F: "))

def f_to_c(f):
    return 5*(f-32)/9

c = f_to_c(f)

print(f"{round(c, 2)}°C")