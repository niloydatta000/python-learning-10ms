# Determining Factorial Using def Function

def factorial(number): # Declaring the function
    if number == 0: # Condition 1
        return 1
    elif number < 0: # Condition 2
        return "Invalid number. Your number must be a positive integer."
    else: # Condition 3
        fac = 1
        for i in range(1, number + 1):
            fac *= i
        return fac # This return call must be OUTSIDE for loop but INSIDE else loop

checkFactorial = int(input("Enter the number to check its factorial: "))
# Print the final result now:
print(f"{checkFactorial}! = {factorial(checkFactorial)}")