# day2.py
# This program calculates the average of three numbers provided by the user.
"""
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("The average of the three numbers is:", average)
"""
# This program checks if a word is a keyword in Python and lists all keywords.
"""
import keyword  as kw
b= kw.iskeyword("lambda")
print("Is 'lambda' a keyword in Python?", b)
b= kw.iskeyword("hello")
print("Is 'hello' a keyword in Python?", b)
b= kw.kwlist
print("List of Python keywords:", b)
"""
# This program demonstrates the use of the 'keyword' module in Python.
# PEMDAS () ** * / + -
#() is for grouping 
# ** is for exponentiation
# * is for multiplication
# / is for division
# + is for addition
# // is for integer division
# - is for subtraction
# print((5 + 3))
# print ((5 + 3) ** 2)
# print((5 + 3) ** 2 - 6 + 3)
# This program demonstrates the use of the 'math' module in Python.

#print(1234%100)

# This program calculates the remainder of 1234 divided by 100.
# by using this we git last two digits of a number.

# chick if a numner is divisible by 5 or not  user input
"""
num = int(input("Enter a number: "))
if num % 5 == 0:    
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")
"""
# This program checks if a number is divisible by 5.

#print hello 100 times
"""
for i in range(100):
    print("Hello")
"""
#program to prints "Hello" 100 times in single line.
"""
for i in range(100):
    print("Hello", end=' ')
"""
"""
# 1 to 10  
for i in range(1, 11):
    print(i, end=' ')
# 10 to 1
print()
for i in range(10, 0, -1):
    print(i, end=' ')
print()
# 1 to 10 even numbers
for i in range(2, 11, 2):
    print(i, end=' ')
print()
# 1 to 10 odd numbers
for i in range(1, 10, 2):
    print(i, end=' ')
print()
"""
"""

# example of boolean expression
print("5>3",5 > 3)  # True  > greater than comparison operator
print("5<3",5 < 3)  # False < less than comparison operator
print("5==3",5 == 3)  # False == equality comparison operator
print("5!=3",5 != 3)  # True != not equal comparison operator
print("5>=3",5 >= 3)  # True >= greater than or equal to comparison operator
print("5<=3",5 <= 3)  # False <= less than or equal to comparison operator
print("5 is 3", 5 is 3)  # False is identity operator
print("5 is not 3", 5 is not 3)  # True is not identity operator
# This program demonstrates various boolean expressions in Python.
# example of logical operators
print("True and True", True and True)  # True and logical AND operator
print("True and False", True and False)  # False and logical AND operator
print("False and True", False and True)  # False and logical AND operator
print("False and False", False and False)  # False and logical AND operator
print("True or True", True or True)  # True or logical OR operator
print("True or False", True or False)  # True or logical OR operator
print("False or True", False or True)  # True or logical OR operator
print("False or False", False or False)  # False or logical OR operator
print("not True", not True)  # False not logical NOT operator
print("not False", not False)  # True not logical NOT operator
# This program demonstrates various logical operators in Python.
# example of bitwise operators
print("5 & 3", 5 & 3)  # 1 & bitwise AND operator
print("5 | 3", 5 | 3)  # 7 | bitwise OR operator
print("5 ^ 3", 5 ^ 3)  # 6 ^ bitwise XOR operator
print("~5", ~5)  # -6 ~ bitwise NOT operator
print("5 << 1", 5 << 1)  # 10 << left shift operator
print("5 >> 1", 5 >> 1)  # 2 >> right shift operator
# This program demonstrates various bitwise operators in Python.
# example of assignment operators
a = 5   # Assignment operator   
b = 3   # Assignment operator
print("a =", a)
print("b =", b)
a += b  # a = a + b
print("a += b:", a)  # 8
a -= b  # a = a - b
print("a -= b:", a)  # 5
a *= b  # a = a * b
print("a *= b:", a)  # 15
a /= b  # a = a / b
print("a /= b:", a)  # 5.0
a //= b  # a = a // b
print("a //= b:", a)  # 1.0
a %= b  # a = a % b
print("a %= b:", a)  # 1.0
a **= b  # a = a ** b
print("a **= b:", a)  # 1.0
a &= b  # a = a & b
print("a &= b:", a)  # 1.0
a |= b  # a = a | b
print("a |= b:", a)  # 3.0
a ^= b  # a = a ^ b
print("a ^= b:", a)  # 2.0
a <<= 1  # a = a << 1
print("a <<= 1:", a)  # 4.0
a >>= 1  # a = a >> 1
print("a >>= 1:", a)  # 2.0
# This program demonstrates various assignment operators in Python.
# example of membership operators
print("'a' in 'apple'", 'a' in 'apple')  # True in membership operator
print("'b' in 'apple'", 'b' in 'apple')  # False in membership operator
print("'a' not in 'apple'", 'a' not in 'apple')  # False not in membership operator
print("'b' not in 'apple'", 'b' not in 'apple')  # True not in membership operator
# This program demonstrates various membership operators in Python.
a = ["apple", "banana", "cherry"]
print( "apple" in a) # True in membership operator
print( "banana" not in a) # False not in membership operator
print ("grape" in a) # False in membership operator
print ("grape" not in a) # True not in membership operator
"""
"""
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a>0 and b>0:
    print("Both numbers are positive.")
elif a<0 and b<0:
    print("Both numbers are negative.")
elif a == 0 and b == 0:
    print("Both numbers are zero.")
elif a > 0 and b < 0:
    print("The first number is positive and the second number is negative.")
elif a < 0 and b > 0:
    print("The first number is negative and the second number is positive.")
else:
    print("One number is zero and the other is either positive or negative.")
"""
# This program checks the positivity or negativity of two numbers provided by the user.
"""
a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
if a>0 or b>0:
    print("At least one number is positive.")
elif a<0 or b<0:
    print("At least one number is negative.")
elif a == 0 or b == 0:
    print("At least one number is zero.")
else:
    print("Both numbers are either positive or negative.")
"""
# bitwise operators
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a, "&", b, "=", a & b)  # Bitwise AND
print(a, "|", b, "=", a | b)  # Bitwise OR
print(a, "^", b, "=", a ^ b)  # Bitwise XOR
print("~", a, "=", ~a)  # Bitwise NOT
print("~", b, "=", ~b)  # Bitwise NOT
print(a, "<< 1 =", a << 1)  # Left shift
print(a, ">> 1 =", a >> 1)  # Right shift
"""
"""
a= 12
b= 12
print(a is b)  # checks if two variables point to the same object in memory.
print(id(a), id(b))  # Print memory addresses
print(id(a) == id(b))  # Check if memory addresses are the same
"""

'''
# check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

#check if year is leap year or not
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
str1= input("Enter a string: ")
vowel_count = count_vowels(str1)
print(f"The number of vowels in '{str1}' is: {vowel_count}")
'''
'''
# there ar 5280 feet in a mile. write a program to convert miles to feet.
miles = float(input("Enter miles: "))
feet = miles * 5280
print(f"{miles} miles is equal to {feet} feet.")
'''
# number of seconds in hours,minutes and seconds
enterd_time = input("Enter time in HH:MM:SS format: ")
hours, minutes, seconds = map(int, enterd_time.split(':'))
total_seconds = hours * 3600 + minutes * 60 + seconds
print(f"Total seconds in {enterd_time} is: {total_seconds} seconds.")