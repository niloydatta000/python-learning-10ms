number = int(input("Enter Max Integer (Starting from 0): "))

i = 0
while i <= number:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i += 1  # This expression is crucial to avoid infinity loop