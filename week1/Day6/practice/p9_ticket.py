# Ask age and 'weekend? (yes/no)'. Under 5 free; 5-17 Rs 100; 18-59 Rs 200; 60+ Rs
#120. Weekend adds Rs 50 (except for free tickets).
age = int(input("Enter the age:"))
weekend = input("Is it weekend? (yes/no):").strip().lower()
if age < 5:
    print("Ticket is free.")
elif age <= 17:
    ticket_price = 100
    if weekend == "yes":
        ticket_price += 50
    print(f"Ticket price is Rs {ticket_price}.")
elif age <= 59:
    ticket_price = 200
    if weekend == "yes":
        ticket_price += 50
    print(f"Ticket price is Rs {ticket_price}.")
else:
    ticket_price = 120
    if weekend == "yes":
        ticket_price += 50
    print(f"Ticket price is Rs {ticket_price}.")
