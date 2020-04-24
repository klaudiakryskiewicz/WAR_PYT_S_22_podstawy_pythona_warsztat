import random

code_str = input("Insert the code: ")
code = []

for i in range(len(code_str)):
    if code_str[i] != " ":
        code.append(code_str[i])

try:
    index_D = code.index("D")
    index_plus = code.index("+")

    x_list = code[:index_D]
    y_list = code[index_D + 1:index_plus]
    z_list = code[index_plus + 1:]

    x = int("".join(x_list))
    y = int("".join(y_list))
    z = int("".join(z_list))

except ValueError:
    print("Invalid code")
    quit()


def dice_roll(y, z, x=1):
    sumd = 0
    for i in range(x):
        sumd += random.randint(1, y)
    return sumd + z


print("Result:", dice_roll(y, z, x))
