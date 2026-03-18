# 4. Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(n) = 1 + 2 + 3 + 4......n - 1 + n

'''


def sum(n):
    if n == 1:
        return 1
    return sum(n - 1) + n

n = int(input("Enter the number: "))

print(f"Sum of first n numbers is: {sum(n)}")