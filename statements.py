# ==========================================================
# 1. Check whether a number is positive, negative, or zero
# ==========================================================

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# ==========================================================
# 2. Assign grades based on marks
# ==========================================================

marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 75 and marks <= 89:
    print("Grade B")
elif marks >= 60 and marks <= 74:
    print("Grade C")
elif marks >= 40 and marks <= 59:
    print("Grade D")
elif marks >= 0 and marks < 40:
    print("Fail")
else:
    print("Invalid Marks")


# ==========================================================
# 3. Check whether a person is a child, teenager,
#    adult, or senior citizen based on age
# ==========================================================

age = int(input("Enter age: "))

if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior Citizen")
else:
    print("Invalid Age")


# ==========================================================
# 4. Check whether a number is one-digit, two-digit,
#    three-digit, or more than three-digit
# ==========================================================

number = int(input("Enter a number: "))

number = abs(number)

if number >= 0 and number <= 9:
    print("One-digit number")
elif number >= 10 and number <= 99:
    print("Two-digit number")
elif number >= 100 and number <= 999:
    print("Three-digit number")
else:
    print("More than three-digit number")


# ==========================================================
# 5. Check whether a customer can withdraw money
# ==========================================================

correct_pin = 1234
balance = 5000

pin = int(input("Enter PIN: "))
amount = float(input("Enter withdrawal amount: "))

if pin == correct_pin:
    if amount <= balance:
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")


# ==========================================================
# 6. Check whether a scholarship is awarded
# ==========================================================

marks = float(input("Enter percentage: "))
income = float(input("Enter family income: "))

income_limit = 300000

if marks >= 85:
    if income < income_limit:
        print("Scholarship Awarded")
    else:
        print("Scholarship Not Awarded")
else:
    print("Scholarship Not Awarded")


# ==========================================================
# 7. Check whether an online order is confirmed
# ==========================================================

stock = input("Is stock available? (yes/no): ")
payment = input("Is payment successful? (yes/no): ")

if stock == "yes":
    if payment == "yes":
        print("Order Confirmed")
    else:
        print("Payment Failed")
else:
    print("Out of Stock")


# ==========================================================
# 8. Check whether an employee is eligible for a bonus
# ==========================================================

service = int(input("Enter years of service: "))
rating = int(input("Enter performance rating (1-5): "))

if service >= 5:
    if rating >= 4:
        print("Eligible for Bonus")
    else:
        print("Not Eligible for Bonus")
else:
    print("Not Eligible for Bonus")