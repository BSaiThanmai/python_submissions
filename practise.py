# Practice questions in simple if and if else. (Total-20Questions)
# Write a program to check whether a number is positive.
# /# Write a program to check whether a number is positive or negative.
num=int(input("Enter a number:"))
if num>0:
 print("postive number",num)
else:
 print("negative number",num)
print("1/11----------------------------------1/11")
# Write a program to check whether a person is eligible to vote (age ≥ 18).
# Write a program to check whether a person is eligible to vote or not.
age=int(input("enter your age:"))
if age>=18:
 print("Eligible to vote",age)
else:
 print("Not Eligible to vote",age)
 print("2/13----------------------------------2/13")
# Write a program to check whether a number is divisible by 5.
div=int(input("Enter a number:"))
if div%5==0:
 print("Divisible BY 5 is",div)
else:
 print("NOT Divisible BY 5",div)
 print("3----------------------------------3")
# Write a program to display "Even Number" if the entered number is even.
# Write a program to check whether a number is even or odd.
ev=int(input("Enter a Number:"))
if ev%2==0:
 print("Even Number",ev)
else:
 print("Odd Number",ev)
 print("4/12----------------------------------4/12")
# Write a program to check whether a student has passed if the marks are 35 or above.
# Write a program to check whether a student has passed or failed (passing marks: 35).
student=int(input("Enter Student Marks :"))
if student>=35:
 print("Student got passed",student)
else:
 print("Student has Failed",student)
print("5/14----------------------------------5/14")
# Write a program to check whether the temperature is greater than 40°C and display "Very Hot".
temperature=float(input("Enter Temp :"))
if temperature>40:
 print("Very Hot",temperature)
else:
 print("Normal Condition",temperature)
print("6----------------------------------6")
# Write a program to check whether a character is 'A'.
character=input("Enter a char :")
if character=='A':
 print("A is EXSIT IN",character)
else:
 print("A Does'nt EXIST",character)
print("7----------------------------------7")
# Write a program to check whether the entered salary is greater than ₹50,000 and display "High Salary".
salary=int(input("Enter Salary Amount :"))
if salary>=50000:
 print("High Salary")
else:
 print("Low Salary")
print("8----------------------------------8")
# Write a program to check whether a person's height is greater than 170 cm.
height=float(input("Enter Your Height :"))
if height>=170:
 print("Tall Height")
else:
 print("Short Height")
print("9----------------------------------9")
# Write a program to check whether the entered password is "python123".
password=str(input("Enter Your Password :"))
if password == 'python123':
 print("Your Password is Correct")
else:
 print("InCorrect Password")
print("10----------------------------------10")
# Write a program to find the greater of two numbers.
num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
if num1>num2:
 print(num1,"is greater number than",num2)
else:
 print(num2,"is greater than",num1)
print("15----------------------------------15")
# Write a program to check whether a number is divisible by 10 or not.
check=int(input("Enter a number :"))
if check%10==0:
 print(check,"is divisible by 10")
else:
 print(check,"is not divisible by 10")
print("16----------------------------------16")
# Write a program to check whether a person is a minor or an adult (18 years or above is an adult).
name=(input("Enter Your Name :"))
person=int(input("Enter an age :"))
if person>=18:
 print(name,"age is",person,"person is Adult")
else:
 print(name,"age is",person,"person is Minor")
print("17----------------------------------17")
# Write a program to check whether the entered username is "admin" or not.
user_name=input("Enter User Name: ")
if user_name=='admin':
 print("UserName Is Correct",user_name)
else:
 print("In-Correct UserName",user_name)
print("18----------------------------------18")
# Write a program to check whether the entered amount is greater than or equal to ₹1000. 
# If yes, display "Discount Applied"; otherwise, display "No Discount".
amount=float(input("Enter an amount: "))
if amount>=1000:
 print("Discount Applied for",amount,"RS")
else:
 print("NO Discount Applied for",amount,"RS")
print("19----------------------------------19")
# Write a program to check whether the entered year is 2026. 
# If yes, display "Current Year"; otherwise, display "Different Year".
year=int(input("Enter an Year: "))
if year==2026:
 print("Current Year is",year)
else:
 print("Different Year ",year)
print("20----------------------------------20")