#Ask three sides. Print 'Not a triangle' if the sum of any two sides is not greater than
#the third. Otherwise print equilateral, isosceles or scalene.

side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
    print("Not a triangle.")
elif side1 == side2 == side3:
    print("Equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle.")
else:
    print("Scalene triangle.")