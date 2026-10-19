#Ask a temperature in Celsius. Print it in Fahrenheit with 1 decimal. (F = C * 9 / 5 +
#32)
celsius = float(input("Enter the temperature in celsius:"))
fahrenheit = celsius * 9 / 5 + 32
print(f"Temperature in fahrenheit: {fahrenheit:.1f}")