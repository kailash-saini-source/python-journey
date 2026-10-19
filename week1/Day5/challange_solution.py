# write one program that asks a 4-digit number and prints its digits reversed using //
#and %.
number = int(input("Enter a 4-digit number:"))
digit1 = number // 1000
digit2 = (number % 1000) // 100
digit3 = (number % 100) // 10
digit4 = number % 10
print(f"Reversed number: {digit4}{digit3}{digit2}{digit1}")