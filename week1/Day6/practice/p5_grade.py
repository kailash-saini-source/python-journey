#Ask marks. Print grade A (90+), B (75+), C (50+), Fail. Test every boundary.
marks = float(input("Enter the marks:"))

if marks > 90:
    print("Grade A")
elif marks > 75:
    print("Grade B")
elif marks > 50:
    print("Grade C")
else:
    print("Fail")