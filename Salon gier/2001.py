from random import randint

user_points = 0
ai_points = 0

#1tura
input("Press enter to roll a dice")
user_round_points = randint(1,6) + randint(1,6)
user_points += user_round_points

ai_round_points = randint(1,6) + randint(1,6)
ai_points += ai_round_points

print(f"Results: Player: {user_points} points, Computer: {ai_points} points")
while ai_points < 2001 and user_points < 2001:
    input("Press enter to roll a dice")
    user_round_points = randint(1, 6) + randint(1, 6)
    if user_round_points == 7:
        user_points = user_points//7
    elif user_round_points == 11:
        user_points = user_points * 11
    else:
        user_points += user_round_points

    ai_round_points = randint(1, 6) + randint(1, 6)
    if ai_round_points == 7:
        ai_points = ai_points // 7
    elif user_round_points == 11:
        ai_points = ai_points * 11
    else:
        ai_points += ai_round_points

    print(f"Results: Player: {user_points} points, Computer: {ai_points} points")


