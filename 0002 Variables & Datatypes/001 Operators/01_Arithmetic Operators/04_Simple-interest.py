#  4. Simple Interest Program

principal = float(input("Enter principal: "))
rate      = float(input("Enter rate (%): "))
time      = float(input("Enter time (years): "))

simple_interest = (principal * rate * time) / 100

print(f"Simple Interest: {simple_interest}")