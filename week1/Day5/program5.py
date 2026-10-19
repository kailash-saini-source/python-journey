#Program 5: Circle calculator
#Plan: area = pi * r squared. Circumference = 2 * pi * r. Use the math module.
import math
radius = float(input("Enter the radius of the circle:"))
area = math.pi * radius ** 2
circumfrence = 2 * math.pi * radius
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumfrence:.2f}")