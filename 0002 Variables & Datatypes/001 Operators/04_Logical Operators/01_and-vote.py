# 1. and — Voting Eligibility

age      = int(input("Enter age: "))
citizen  = input("Are you a citizen? (yes/no): ")

if age >= 18 and citizen == "yes":
    print("You are eligible to Vote ")
else:
    print("You are NOT eligible to Vote ")
