#Ask age. Print 'Eligible to vote' if 18 or more, else how many years are left.

age = int(input("Enter the age:"))

if age >= 18:
    print("Eligible to vote.")
else:
    years_left = 18 - age
    print(f"Not eligible to vote. You need to wait {years_left} more years.")