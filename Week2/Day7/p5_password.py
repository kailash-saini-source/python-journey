#Keep asking for the password until it is correct. Count the attempts and print
#'Correct after N attempts

attempts = 0
while True:
    password = input("Enter the password: ")
    attempts += 1
    if password == "python":
        break
    print("Incorrect password. Try again.")

print(f"Correct after {attempts} attempts.")