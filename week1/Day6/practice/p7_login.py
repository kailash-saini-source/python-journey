#Ask username and password. Admin password is saved as python123. Print Welcome,
#Wrong password, or Unknown user.


print("Welcome to the login system.")
username = input("Enter username:")
password = input("Enter password:")

if username == "admin":
    if password == "python123":
        print("Welcome, admin!")
    else:
        print("Wrong password.")
else:
    print("Unknown user.")