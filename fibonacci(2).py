fib = 0
counter = 1

for i in range(10):
    print(fib, end=" ") # This end=" " will make output into one line
    temp = counter
    counter = fib + counter
    fib = temp