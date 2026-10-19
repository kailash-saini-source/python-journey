#Program 1: Greeting card
#Plan: ask name, city, age. Print a card with the name in capitals, the city, and the age next year.
name = input(str("Enter your name:"))
city = input(str("Enter your city:"))
age = int(input("Enter your age:"))

print("= " * 30)
print(f"{name.upper():^30}")
print(f"{city.title():^30}")
print(f"Next year you will be {age + 1} years old.")
print("= " * 30)