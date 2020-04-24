

print("Think of a number between 0 and 1000, I will guess it in less than 10 tries")
min_number = 0
max_number = 1000

guessed = False
while not guessed:
    guess = int((max_number - min_number) / 2) + min_number
    print(f"Zgaduję: {guess} ")
    answer1 = input("Did I guess your number? ")
    if answer1 == "yes":
        print("I won!")
        guessed = True
    elif answer1 == "no":
        answer2 = input("Is it too big? ")
        if answer2 == "yes":
            max_number = guess
        elif answer2 == "no":
            answer2 = input("Is it too small? ")
            if answer2 == "yes":
                min_number = guess
            elif answer2 == "no":
                print("nie oszukuj!")