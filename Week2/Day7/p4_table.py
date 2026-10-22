#Ask a number. Print its table 1 to 10 like 7 x 3 = 21
num = int(input("Enter a whole number: "))

i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1