import random
winner = ''
random_choice = random.randint(0,2)
if random_choice == 0:
    pc_choice = ("rock")
elif random_choice == 0:
    pc_choice = ("paper")
else:
    pc_choice = ("scissors")

player_choice = input("rock, paper or scissors?")
if pc_choice == player_choice:
    winner = "Draw"
elif pc_choice == "paper" and player_choice == "rock":
    winner = "PC"
elif pc_choice == "rock" and player_choice == "scissors":
    winner = "PC"
elif pc_choice == "scissors" and player_choice == "paper":
    winner = "PC"
else:
    winner = "Player"
print ("Machine's choice","=",pc_choice)

print ("The winner is:",winner)
