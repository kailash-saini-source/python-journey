#Ask an amount in INR and the INR-per-dollar rate. Print the dollars with 2 decimals.
amount_inr = float(input("Enter the amount in INR:"))
rate = float(input("Enter the INR-per-dollar rate:"))
dollars = amount_inr / rate
print(f"Amount in dollars: {dollars:.2f}")