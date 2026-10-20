#The program asks for two numbers and an operator. It supports + - * / // % **.
#It prints the full expression and the result, for example: 8.0 + 5.0 = 13.0
#Dividing by zero (for / // %) must print a friendly error, not crash.
#An unknown operator must print a friendly error.
#Plan (IPO): INPUT num1, operator, num2. PROCESS choose the calculation with if / elif. OUTPUT the result or an
#error message

print("==== Mini Calculator ====")
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /, //, %, **): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")

elif operator == "//":
    if num2 ==0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")

elif operator == "%":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")

elif operator == "**":
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")

else:
    print("Error: Unknown operator. Please use one of the following: +, -, *, /, //, %, **.")