import random

ai_number = random.randint(1, 100)

guessed = False

while not guessed:
    user_number = input("Guess the number: ")
    try:
        user_number = int(user_number)
    except ValueError:
        print("It's not a number!")
        continue

    if user_number == ai_number:
        print("You win!")
        guessed = True
    elif user_number > ai_number:
        print("Too big!")
    elif user_number < ai_number:
        print("Too small!")
