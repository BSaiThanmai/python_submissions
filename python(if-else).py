# Write a program to check if a user has entered the correct OTP (1234). If correct, display "OTP Verified".
otp = input("Enter OTP: ")
if otp == "1234":
    print("OTP Verified")
else:
    print("Incorrect OTP")
# Write a program to check if the mobile battery percentage is below 20.
# If yes, display "Please Charge Your Phone".
battery = int(input("Enter battery percentage: "))
if battery < 20:
    print("Please Charge Your Phone")
else:
    print("Battery Level OK")
# Write a program to check if a bank account balance is greater than ₹10,000.
# If yes, display "Eligible for Premium Account".
balance = float(input("Enter account balance: "))
if balance > 10000:
    print("Eligible for Premium Account")
else:
    print("Not Eligible for Premium Account")
# Write a program to check if a person has a valid ticket (has_ticket = True).
# If yes, display "Welcome to the Movie".
has_ticket = input("Do you have a ticket? (yes/no): ")
if has_ticket.lower() == "yes":
    print("Welcome to the Movie")
else:
    print("No Ticket, Entry Denied")
# Write a program to check whether a person is eligible to vote.
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")
# Write a program to check whether a customer is eligible for free delivery (bill ≥ ₹1000).
bill = float(input("Enter bill amount: "))
if bill >= 1000:
    print("Eligible for Free Delivery")
else:
    print("Not Eligible for Free Delivery")
# Write a program to check whether a user has enough balance to withdraw ₹5000.
balance = float(input("Enter account balance: "))
if balance >= 5000:
    print("You can withdraw ₹5000")
else:
    print("Insufficient Balance to withdraw ₹5000")
