import random
winner = ''
random_choice = random.randint(0,2)
if random_choice == 0:
    pc_choice = ("piedra")
elif random_choice == 0:
    pc_choice = ("papel")
else:
    pc_choice = ("tijeras")

player_choice = input("piedra, papel o tijeras?")
if pc_choice == player_choice:
    winner = "Empate"
elif pc_choice == "papel" and player_choice == "piedra":
    winner = "PC"
elif pc_choice == "piedra" and player_choice == "tijeras":
    winner = "PC"
elif pc_choice == "tijeras" and player_choice == "papel":
    winner = "PC"
else:
    winner = "Jugador"
print ("Máquina's choice","=",pc_choice)

print ("The winner is:",winner)
