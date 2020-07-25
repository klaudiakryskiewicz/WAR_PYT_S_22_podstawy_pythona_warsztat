from random import randint, choice

user_points = 0
ai_points = 0

# 1tura
dice1 = input("Choose dice 1: D3, D4, D6, D8, D10, D12, D20, D100 ")
dice2 = input("Choose dice 2: D3, D4, D6, D8, D10, D12, D20, D100 ")

dice1_max = int(dice1[1:])
dice2_max = int(dice2[1:])

user_round_points = randint(1, dice1_max) + randint(1, dice2_max)
user_points += user_round_points

list_of_dices = [3, 4, 6, 8, 10, 12, 20, 100]
dice1_max = int(choice(list_of_dices))
dice2_max = int(choice(list_of_dices,))
ai_round_points = randint(1, dice1_max) + randint(1, dice2_max)
ai_points += ai_round_points

print(f"Results: Player: {user_points} points, Computer: {ai_points} points")
while ai_points < 2001 and user_points < 2001:
    dice1 = input("Choose dice 1: D3, D4, D6, D8, D10, D12, D20, D100 ")
    dice2 = input("Choose dice 2: D3, D4, D6, D8, D10, D12, D20, D100 ")

    dice1_max = int(dice1[1:])
    dice2_max = int(dice2[1:])

    user_round_points = randint(1, dice1_max) + randint(1, dice2_max)
    if user_round_points == 7:
        user_points = user_points//7
    elif user_round_points == 11:
        user_points = user_points * 11
    else:
        user_points += user_round_points

    dice1_max = int(choice(list_of_dices))
    dice2_max = int(choice(list_of_dices, ))
    ai_round_points = randint(1, dice1_max) + randint(1, dice2_max)
    if ai_round_points == 7:
        ai_points = ai_points // 7
    elif user_round_points == 11:
        ai_points = ai_points * 11
    else:
        ai_points += ai_round_points

    print(f"Results: Player: {user_points} points, Computer: {ai_points} points")
