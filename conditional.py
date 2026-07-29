        #1. Check Last Digit 
num = int(input("Enter an integer: "))
last_digit = num % 10
if last_digit % 2 == 0:
    print("Even Last Digit")
else:
    print("Odd Last Digit")

    # 2. Check Divisibility of Last Digit
num = int(input("Enter an integer: "))
last_digit = num % 10
if last_digit % 3 == 0:
    print("Last digit is divisible by 3")
else:
    print("Last digit is not divisible by 3")

    # 3. Check Character Type
ch = input("Enter a single character: ")
if ch.isalpha():
    print("Alphabet")
else:
    print("Not an Alphabet")

    # 4. Check Uppercase or Lowercase
ch = input("Enter a single alphabet: ")
if ch.isupper():
    print("Uppercase")
else:
    print("Lowercase")

    # 5. Check Vowel or Consonant
ch = input("Enter a single alphabet: ")
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")
