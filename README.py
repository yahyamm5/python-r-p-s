import random
player = input("Enter your ting!")
choices = ["x", "m", "o"]

player2 = random.choice(choices)


if player == "x" and player2 ==  "m"  :
    print("player win!")
if player == "m" and player2 ==  "x"  :
    print("player2 win!")
if player == "o" and player2 ==  "x"  :
    print("player win!")
if player == "x" and player2 ==  "o"  :
    print("player2 win!")
if player == "m" and player2 ==  "o"  :
    print("player win!")
if player == "o" and player2 ==  "m"  :
    print("player2 win!")
if player == "m" and player2 ==  "m" or player == "o" and player2 == "o" or player == "x" and player2 == "x":
    print("drow!")


print(player,player2)
