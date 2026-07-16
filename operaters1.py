# 1. Arithmetic Operators
#               Accept two numbers and display the results of +, -, , /, //, %, and *.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)

# 2.Assignment Operators
#         Initialize a variable with 50 and perform +=, -=, =, /=, //=, %=, and *= operations, 
#             displaying the value after each operation.
# Assignment Operators
num = 50
print("Initial Value:", num)
num += 10
print("After += 10:", num)
num -= 5
print("After -= 5:", num)
num *= 2
print("After *= 2:", num)
num /= 5
print("After /= 5:", num)
num //= 2
print("After //= 2:", num)
num %= 4
print("After %= 4:", num)


# Comparison Operators
          # Accept two numbers and display the results of ==, !=, >, <, >=, and <=.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Equal:", num1 == num2)
print("Not Equal:", num1 != num2)
print("Greater Than:", num1 > num2)
print("Less Than:", num1 < num2)
print("Greater Than or Equal:", num1 >= num2)
print("Less Than or Equal:", num1 <= num2)

# Logical Operators
num = int(input("Enter a number: "))
print("num > 10 and num < 100:", num > 10 and num < 100)
print("num % 2 == 0 or num % 5 == 0:", num % 2 == 0 or num % 5 == 0)
print("not(num > 50):", not(num > 50))

# Identity Operators
list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = list1
print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("list1 is not list2:", list1 is not list2)
print("list1 == list3:", list1 == list3)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)

# Membership Operators
text = "PYTHON"
ch = input("Enter a character: ").upper()
print(ch, "in PYTHON:", ch in text)
print(ch, "not in PYTHON:", ch not in text)

# Student Marks Calculator

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = (total / 500) * 100
print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage, "%")

# Shopping Bill Calculator
price1 = float(input("Enter price of Product 1: "))
qty1 = int(input("Enter quantity of Product 1: "))

price2 = float(input("Enter price of Product 2: "))
qty2 = int(input("Enter quantity of Product 2: "))

price3 = float(input("Enter price of Product 3: "))
qty3 = int(input("Enter quantity of Product 3: "))

total1 = price1 * qty1
total2 = price2 * qty2
total3 = price3 * qty3
bill = total1 + total2 + total3
print("Product 1 Total:", total1)
print("Product 2 Total:", total2)
print("Product 3 Total:", total3)
print("Grand Total Bill:", bill)
print("Product 1 > Product 2:", total1 > total2)
print("Product 1 < Product 2:", total1 < total2)
print("Product 1 == Product 2:", total1 == total2)

# Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
print("Is Fahrenheit greater than 100?", fahrenheit > 100)

