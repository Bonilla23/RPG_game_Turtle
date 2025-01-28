# Added Libraries [ turtle, time, random ]
import turtle;
import time;
import random;

# Create a variable "wn" 
# For the Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("RPG Game")

# Create variable "texto"
# Use it as text
texto = turtle.Turtle()
texto.color("white")
texto.hideturtle()
texto.penup()
texto.speed(0)

# Create variables 
victorias = 0
vida = 0
vidatotal = 0
daño = 0
agilidad = 0
inteligencia = 0

# function to select a class
def seleccionar_clase():
    global vida,vidatotal,daño,agilidad,inteligencia
    
    clases = {"Mago": (1, 10, 1, 10, 10, 20),
              "Guerrero": (10, 20, 10, 20, 1, 10),
              "Pícaro": (5, 15, 5, 15, 5, 15)}
    
    # To select a class
    while True:
        clase = wn.textinput("Seleccionar Clase", "Elige una clase: Mago, Guerrero o Pícaro").capitalize()
        if clase in clases:
            rangos = clases[clase]
            # Random number
            vida = random.randint(rangos[0], rangos[1])
            daño = random.randint(rangos[2], rangos[3])
            agilidad = random.randint(rangos[4], rangos[5])
            inteligencia = random.randint(rangos[4], rangos[5])
            vidatotal = vida  # To safe the max heal
            return clase
        else:
            # If not select a class
            texto.clear()
            texto.write("Clase no válida. Intenta de nuevo.", align="center", font=("Courier", 24, "normal"))
            time.sleep(2)
            texto.clear()

#Function to generate a monster
def generar_monstruo():
    return {
        "nombre": random.choice(["Esqueleto", "Zombi", "Orco", "Dragón"]),
        "vida": random.randint(5, 20),
        "daño": random.randint(1, 10)
    }