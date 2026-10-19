#Ask price and discount percent. Print the final price and the money saved.
price = float(input("Enter the price of the item:"))
discount_percent = float(input("Enter the discount percent:"))
discount_amount = (discount_percent / 100) * price
final_price = price - discount_amount
print(f"Final price: {final_price:.2f}")
print(f"Money saved: {discount_amount:.2f}")