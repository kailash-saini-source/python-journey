#Ask marks in 5 subjects (out of 100). Print total, average and percentage.
subject1 = float(input("Enter marks in subject 1:"))
subject2 = float(input("Enter marks in subject 2:"))
subject3 = float(input("Enter marks in subject 3:"))
subject4 = float(input("Enter marks in subject 4:"))
subject5 = float(input("Enter marks in subject 5:"))
total = subject1 + subject2 + subject3 + subject4 + subject5
average = total / 5
percentage = (total / 500) * 100
print(f"Total marks: {total:.2f}")
print(f"Average marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")