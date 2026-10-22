#Print even numbers 2 to 50 on one line, separated by spaces

n = 2
while n <= 50:
    if n % 2 == 0:
        print(n, end=" ")
    n += 1