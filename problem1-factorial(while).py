# Solving Problem 1 using while loop instead of for loop

num = int(input("Enter the number to check its factorial: "))

if num < 0: # Condition 1
    print("Invalid number. Your number must be a positive integer.")
elif num == 0: # Condition 2
    print(f"{num}! = 1")
else: # Condition 3
    fac = 1 # Declared here but could be declared at the top
    i = 1
    # Try while loop now
    while i <= num:
        fac *= i
        i += 1 # This statement is crucial to avoid infinity loop
    print(f"{num}! = {fac}") # This statement must be OUTSIDE while loop but INSIDE else loop