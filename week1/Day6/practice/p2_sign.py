#Ask a number. Print positive, negative or zero.
num = float(input("Enter a number:"))
if num > 0:
    print(f"{num} is positive.")
elif num == 0:
    print(f"{num} is zero.")
else:
    print(f"{num} is negative.")