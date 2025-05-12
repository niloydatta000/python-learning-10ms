# Prime number function

def primeNumber(number):
    if number <= 1:
        return False
    else:
        # Now remove all non-prime numbers using the following loop
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


# Let's take a user input:

while True:
    num = int(input("Is the number prime or not?: "))
    prime = primeNumber(num)
    if prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

    # Let's seek user input again in the form of yes or no

    terminator = input("Do you want to continue yes/no: ").strip()
    if terminator.lower().strip() != "yes":
        break