import  random # random is a Built-in Module
aRandomNumber = random.randint(1, 10)  # Range in parenthesis

# Trying to create loop

while True:
    userInput = int(input("Guess a number: "))
    if userInput == aRandomNumber:
        print(f"Well done. {userInput} is the correct number.")
    
    else:
        print("Wrong guess. Try again!")

    terminator = int(input("Press 0 to continue: "))
    if terminator != 0:
         break

# Loop is complete