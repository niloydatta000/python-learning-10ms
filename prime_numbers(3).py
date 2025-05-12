# Prime number function

def primeNumber(number):
    if number > 1:
        prime = True

        # Now remove all non-prime numbers using the following loop
        for i in range(2, number):
            if number %  i == 0:
                prime = False

        if prime:
            return True
        else:
            return False

# Let's take a user input:

num = int(input("Is the number prime or not: "))
print(primeNumber(num))