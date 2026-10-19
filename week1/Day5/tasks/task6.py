#Ask two numbers. Swap them and print both.
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
a , b = b , a
print(f"After swapping: a = {a}, b = {b}")