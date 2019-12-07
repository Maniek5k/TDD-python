import random

player = int(input())

if player > 5:
    print("More than 5")
elif player == 5:
    print("Exactly 5")
else:
    print("Less than 5")

print(random.choice(["Andrzej", "Adam", "Zygmunt"]))
