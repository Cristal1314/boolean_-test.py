#  20 points each challenge...
# problem 1: Check if a number is both even and divisible by 5.
# The program prompts the user for a number, checks whether it meets both conditions 
# (even and divisible by 5), and then outputs the result to the console.

# Prompt the user for a number
user = ("Enter a number")
# Check if the number is even and divisible by 5
if user == ("even"):
    print('Number is even')
else: 
   print("Number is not even")

if user == ('divisible by 5') :
    print('is divisible by 5')
else:
    print('not divisible by 5')
# Output the result to the console

#---------------------------------------------------------------------------------------------------------------------------------------------
# Problem 2: Number in Range
# Description:
# Create a program that checks whether a given number falls within a specified range, such as 10 to 20 (inclusive).

number = ("Enter number:")


#  Output: "The number is within the range." or "The number is outside the range."
if number == ('number => 10 and number <= 20 '):
     print ("The number is within the range." )
else:
    print("The number is outside the range.")

# Hint:
# Use the and operator to check if the number is greater than or equal to 10 and less than or equal to 20.
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Problem 3: Password Strength Checker
# Description:
# Write a program that checks if a user's password meets the following criteria:

# At least 8 characters long

# Contains at least one digit (0-9)

# Input: Password (string)

# Output: "Password is strong." or "Password is weak."
password=("enter a password that has 8 characters :")

if password == (password >= len(8) and password == digit any(0-9)) :
    print("Password is strong")
else:
    print("Password is weak ")
# Hint: 
# Use the len() function to check the length and the any() function with a generator expression to check for a digit.

# --------------------------------------------------------------------------------------------------------------

# Problem 4: Odd or Even and Multiple of 3
# Description:
# Create a program that determines if a number is odd or even and also checks if it is a multiple of 3.

# Input: A number (integer)
problem4 = ('Enter a number')
# Output:
# "Even and a multiple of 3."
if problem4 == 2 or 3:
    print("Even but not a multiple of 3")
elif problem4 != 2 or 3:
    print('Odd and  a multiple of 3')
elif problem4 != 2:
    print('Odd but not a multiple of 3.')
# "Even but not a multiple of 3."
# "Odd and a multiple of 3."
# "Odd but not a multiple of 3."
# Hint:
# Use % for both the even check and the multiple of 3 check.

# ------------------------------------------------------------------------------------------------------------
    
# Problem 5: Vowel or Consonant
# Description:
# Write a program that takes a single character as input and checks whether it is a vowel or a consonant. Assume the input is a lowercase letter.
# Input: A character (string of length 1)
problem5 = "Enter a letter"
# Output: "Vowel" or "Consonant"
if problem5 == ['a', 'i', 'e', 'o','u']:
    print('letter is a vowel')
else:
    print('Letter is a constant')
# Hint:
# Use the in operator to check if the character belongs to the set {'a', 'e', 'i', 'o', 'u'}.