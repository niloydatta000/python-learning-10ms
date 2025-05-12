# Prime numbers in between 1 to 100

for i in range(100): # Fixing the Range
    if i > 1:
        prime = True

        # Now remove non-prime numbers the whole for loop below using break

        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime: # Indentation is important...
            print(i)