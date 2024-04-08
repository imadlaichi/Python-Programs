import random
print("Bienvenido a Madinator, piensa en un personaje de Avengers Infinity War y yo lo adivinaré.")
print("Los personajes que puedo adivinar son: Spiderman, Ironman, Capitan America, Hulk, Thor, Black Panther, Black Widow, Nebula, Vision, Groot")

database = [
    {"name": "Spiderman", "Hombre": True, "Humano": True, "Ciborg": False, "Avengers Classics": False, "Dios": False, "Vocabulario_limitado": False, "Arma_Escudo": False, "Escalar": True, "Volar": False},
    {"name": "Ironman", "Hombre": True, "Humano": True, "Ciborg": False, "Avengers Classics": True, "Dios": False, "Vocabulario_limitado": False, "Arma_Escudo": False, "Escalar": False, "Volar": True},
    {"name": "Capitan America", "Hombre": True, "Humano": True, "Ciborg": False, "Avengers Classics": True, "Dios": False, "Vocabulario_limitado": False, "Arma_Escudo": True, "Escalar": False, "Volar": False},
    {"name": "Hulk", "Hombre": True, "Humano": True, "Ciborg": False, "Avengers Classics": True, "Dios": False, "Vocabulario_limitado": False, "Arma_Escudo": False, "Escalar": False, "Volar": False},
    {"name": "Thor", "Hombre": True, "Humano": False, "Ciborg": False, "Avengers Classics": True, "Dios": True, "Vocabulario_limitado": False, "Arma_Escudo": True, "Escalar": False, "Volar": True},
    {"name": "Black Panther", "Hombre": True, "Humano": True, "Ciborg": False, "Avengers Classics": False, "Dios": False, "Vocabulario_limitado": False, "Arma_Escudo": True, "Escalar": False, "Volar": False},
    {"name": "Black Widow", "Hombre": False, "Humano": True, "Ciborg": False, "Avengers Classics": False, "Dios": False, "Vocabulario_limitado": False, "Arma_Escudo": True, "Escalar": False, "Volar": False},
    {"name": "Nebula", "Hombre": False, "Humano": False, "Ciborg": True, "Avengers Classics": False, "Dios": False, "Vocabulario_limitado": False, "Arma_Escudo": False, "Escalar": False, "Volar": False},
    {"name": "Vision", "Hombre": True, "Humano": False, "Ciborg": False, "Avengers Classics": False, "Dios": False, "Vocabulario_limitado": False, "Arma_Escudo": False, "Escalar": False, "Volar": False},
    {"name": "Groot", "Hombre": True, "Humano": False, "Ciborg": False, "Avengers Classics": False, "Dios": False, "Vocabulario_limitado": True, "Arma_Escudo": False, "Escalar": False, "Volar": False},
]

def tomar_posibilidad(respuesta, propiedad):
 
    if respuesta == "si":
        ans = True
    else:
        ans = False
        
    a_eliminar=[]
    for d in database:
        if d[propiedad] != ans:
            a_eliminar.append(d)
            
    for i in a_eliminar:
        database.remove(i)
        
    if len(database) == 1:
        print("Tu personaje es " + database[0]["name"])
        quit()


preguntas = [
    ("¿Tu personaje es masculino? (si, no): ", "Hombre"),
    ("¿Tu personaje es humano? (si, no): ", "Humano"),
    ("¿Tu personaje es mitad ciborg? (si, no): ", "Ciborg"),
    ("¿Tu personaje forma parte de los Avengers clásicos? (si, no): ", "Avengers Classics"),
    ("¿Tu personaje es un dios? (si, no): ", "Dios"),
    ("¿Tu personaje tiene vocabulario limitado? (si, no): ", "Vocabulario_limitado"),
    ("¿Tu personaje tiene alguna arma o escudo? (si, no): ", "Arma_Escudo"),
    ("¿Tu personaje puede escalar paredes? (si, no): ", "Escalar"),
    ("¿Tu personaje puede volar? (si, no): ", "Volar")
]
random.shuffle(preguntas)

for pregunta, propiedad in preguntas:
    respuesta = input(pregunta)
    tomar_posibilidad(respuesta, propiedad)
