# Determination of a prime number:

num = int(input("Enter your number: "))

if num > 1:
    prime = True

    # Now remove all non-prime numbers using the following loop
    for i in range(2, num):
        if num %  i == 0:
            prime = False

    # Print the final expression now

    if prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is a not prime number.")