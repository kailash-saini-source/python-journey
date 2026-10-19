# Program 4: Simple interest
# Plan: interest = principal * rate * years / 100. Show interest and total amount with commas.
principal = float(input("Enter the principal amount:"))
rate = float(input("Enter the rate of interest (in %):"))
years = float(input("Enter the number of years:"))
intrest = principal * rate * years / 100
total_amount = principal + intrest
print(f"intrest: {intrest:,.2f}")
print(f"total amount:{total_amount:,.2f}")