#Ask birth year. Print the age in 2026, and the approximate age in months and in
#days.
dob = int(input("Enter your birth year:"))
age = 2026 - dob
age_in_monts = age * 12
age_in_days = age * 365
print(f"Your age in 2026: {age} years")
print(f"Your approximate age in months: {age_in_monts} months")
print(f"Your approximate age in days: {age_in_days} days")