import random

i = 0
number_list = []
while i < 6:
    number = input(f"Give me {i + 1} number: ")
    try:
        number = int(number)
    except ValueError:
        print("It's not a number")

    if type(number) == int and number not in range(1, 50):
        print("You can only choose number between 1 and 49")
    elif number in number_list:
        print("You can choose this number only once")
    elif number in range(1, 50):
        number_list.append(number)
        i += 1

number_list.sort()
print(number_list)

ai_list = random.sample(range(1, 50), 6)
ai_list.sort()
print(ai_list)


no_of_guessed = 0
for number in number_list:
    if number in ai_list:
        no_of_guessed += 1


print(f"You guessed {no_of_guessed} numbers!")
