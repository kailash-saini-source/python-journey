#Ask a 3-digit number. Print the sum of its digits using // and %.
number = int(input("Enter a 3-digit number:"))
digit1 = number // 100
digit2 = (number % 100) // 10
digit3 = number % 10
sum_of_digits = digit1 + digit2 + digit3
print(f"Sum of digits: {sum_of_digits}")
