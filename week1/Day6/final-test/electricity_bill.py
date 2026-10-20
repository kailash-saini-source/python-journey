# Ask the units used. First 100 units cost Rs 3 each, the next 100 units
#Rs 5 each, and units above 200 cost Rs 8 each. Print the bill. (Example: 250 units = 1200.)

units = int(input("Enter the number of units used:"))
if units <= 100:
    print(f"Bill amount is Rs {units * 3}")
elif units <= 200:
    bill_amount = (100 *3 ) + ((units-100) * 5)
    print(f"Bill amount is Rs {bill_amount}")
else:
    bill_amount = (100 * 3) + (100 * 5) + ((units - 200) * 8)
    print(f"Bill amount is Rs {bill_amount}")  