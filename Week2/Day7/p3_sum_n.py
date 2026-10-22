#Ask n. Print sum of 1 to n (n = 100 gives 5050)
n = int(input("Enter a whole number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(f"Sum of 1 to {n} is {total}")