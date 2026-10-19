# Program 2: Bill splitter
#Plan: input bill, tip percent, number of people. Process: tip = bill * percent / 100, total = bill + tip, share
#= total / people. Output: total and share with 2 decimals.
bill = float(input("Enter the bill amount:"))
tip_percent = float(input("Enter the tip percentage:"))
people = int(input("Enter the number of people:"))
tip = bill * tip_percent / 100
total = bill + tip
share = total / people
print(f"Total bill including tip: ${total:.2f}")
print(f"Each person should pay: ${share:.2f}")