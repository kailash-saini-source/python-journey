# Ask a number of minutes. Print it as days, hours and minutes.
#(Example: 3000 minutes = 2 days 2 hours 0 minutes.)

num = int(input("Enter the number of minutes: "))
num_days = num // (24 * 60)
num_hours = (num % (24 * 60)) // 60
num_minutes = num % 60
print(f"{num_days} days {num_hours} hours {num_minutes} minutes")
