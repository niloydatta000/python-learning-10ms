""" Problem:
Write a python program to calculate the factorial of a non-negative number n.
Which is the product of all positive integers less than equal to n.
Factorial of 0 is 1.
"""
#Solution:

num = int(input("Enter the number to check its factorial: "))

if num < 0: # Condition 1
    print("Invalid number. Your number must be a positive integer.")
elif num == 0: # Condition 2
    print(f"{num}! = 1")
else: # Condition 3
    fac = 1 # Declared here but could be declared at the top
    for i in range(1, num + 1):
        fac *= i
    print(f"{num}! = {fac}") # This statement must be OUTSIDE for loop but INSIDE else loop