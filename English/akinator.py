import random
print("Welcome to Madinator, think of a character from Avengers Infinity War and I will guess it.")
print("The characters I can guess are: Spiderman, Ironman, Captain America, Hulk, Thor, Black Panther, Black Widow, Nebula, Vision, Groot")

database = [
    {"name": "Spiderman", "Male": True, "Human": True, "Cyborg": False, "Avengers_Classics": False, "God": False, "Limited_Vocabulary": False, "Weapon_Shield": False, "Climb": True, "Fly": False},
    {"name": "Ironman", "Male": True, "Human": True, "Cyborg": False, "Avengers_Classics": True, "God": False, "Limited_Vocabulary": False, "Weapon_Shield": False, "Climb": False, "Fly": True},
    {"name": "Captain America", "Male": True, "Human": True, "Cyborg": False, "Avengers_Classics": True, "God": False, "Limited_Vocabulary": False, "Weapon_Shield": True, "Climb": False, "Fly": False},
    {"name": "Hulk", "Male": True, "Human": True, "Cyborg": False, "Avengers_Classics": True, "God": False, "Limited_Vocabulary": False, "Weapon_Shield": False, "Climb": False, "Fly": False},
    {"name": "Thor", "Male": True, "Human": False, "Cyborg": False, "Avengers_Classics": True, "God": True, "Limited_Vocabulary": False, "Weapon_Shield": True, "Climb": False, "Fly": True},
    {"name": "Black Panther", "Male": True, "Human": True, "Cyborg": False, "Avengers_Classics": False, "God": False, "Limited_Vocabulary": False, "Weapon_Shield": True, "Climb": False, "Fly": False},
    {"name": "Black Widow", "Male": False, "Human": True, "Cyborg": False, "Avengers_Classics": False, "God": False, "Limited_Vocabulary": False, "Weapon_Shield": True, "Climb": False, "Fly": False},
    {"name": "Nebula", "Male": False, "Human": False, "Cyborg": True, "Avengers_Classics": False, "God": False, "Limited_Vocabulary": False, "Weapon_Shield": False, "Climb": False, "Fly": False},
    {"name": "Vision", "Male": True, "Human": False, "Cyborg": False, "Avengers_Classics": False, "God": False, "Limited_Vocabulary": False, "Weapon_Shield": False, "Climb": False, "Fly": False},
    {"name": "Groot", "Male": True, "Human": False, "Cyborg": False, "Avengers_Classics": False, "God": False, "Limited_Vocabulary": True, "Weapon_Shield": False, "Climb": False, "Fly": False},
]

def take_chance(answer, property):
 
    if answer == "yes":
        ans = True
    else:
        ans = False
        
    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)
            
    for i in to_remove:
        database.remove(i)
        
    if len(database) == 1:
        print("Your character is "+database[0]["name"])
        quit()


questions = [
    ("Is your character male? (yes, no): ", "Male"),
    ("Is your character human? (yes, no): ", "Human"),
    ("Is your character half cyborg? (yes, no): ", "Cyborg"),
    ("Does your character belong to the classic Avengers? (yes, no): ", "Avengers_Classics"),
    ("Is your character a god? (yes, no): ", "God"),
    ("Does your character have limited vocabulary? (yes, no): ", "Limited_Vocabulary"),
    ("Does your character have any weapon or shield? (yes, no): ", "Weapon_Shield"),
    ("Can your character climb walls? (yes, no): ", "Climb"),
    ("Can your character fly? (yes, no): ", "Fly")
]
random.shuffle(questions)

for question, property in questions:
    ans = input(question)
    take_chance(ans, property)
