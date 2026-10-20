#. Ask a whole number. If it is divisible by both 3 and 5 print FizzBuzz; if
#only by 3 print Fizz; if only by 5 print Buzz; otherwise print the number.

num = int(input("Enter a whole number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)