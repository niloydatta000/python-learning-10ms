number = int(input("Enter Max Integer (Starting from 0): "))

for i in range(0, number + 1): # Using for loop to avoid infinity loop trap
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")