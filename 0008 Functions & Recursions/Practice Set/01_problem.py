# 1. Write a program using functions to find greatest of three numbers.



def greatest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
        
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))
        
print(f"The greatest number is: {greatest(num1, num2, num3)}")    