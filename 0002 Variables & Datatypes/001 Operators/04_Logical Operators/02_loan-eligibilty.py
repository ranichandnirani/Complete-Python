# 2. (and) — Loan Eligibility

age    = int(input("Enter age: "))
salary = int(input("Enter monthly salary: ₹"))
score  = int(input("Enter credit score: "))

if age >= 21 and salary >= 25000 and score >= 700:
    print("Loan Approved ")
else:
    print("Loan Rejected ")