import random


a_random_number = random.randint(1, 10)

count = 0
print("Welcome to the number guessing game!")
while count < 3:
    print(f"You have {3 - count} tries to guess the number.")
    user_input = int(input("Guess a number between 1 and 10: "))
    count += 1
    if user_input == a_random_number:
        print(f"Congratulations! {user_input} is the correct number. You guessed the number in {count} tries.")
        break
    else:
        if count == 3:
            print(f"Sorry! You've used all your tries. The correct number was {a_random_number}.")
        else:
            print("Try again!")S