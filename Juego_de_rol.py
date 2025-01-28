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

# Function to show the statistics
def mostrar_estadisticas(jugador, monstruo):
    texto.clear()
    texto.goto(0, 200)
    texto.write(f"Tu Vida: {vida} | Daño: {daño} | Agilidad: {agilidad} | Inteligencia: {inteligencia}", align="center", font=("Courier", 18, "normal"))
    texto.goto(0, 150)
    texto.write(f"Monstruo: {monstruo['nombre']} | Vida: {monstruo['vida']} | Daño: {monstruo['daño']}", align="center", font=("Courier", 18, "normal"))
    time.sleep(2)
    
# Función para combatir
def combatir(jugador, monstruo):
    global vida, victorias

    texto.clear()
    texto.goto(0, 200)
    texto.write(f"¡Un {monstruo['nombre']} aparece con {monstruo['vida']} de vida!", align="center", font=("Courier", 24, "normal"))
    time.sleep(2)

    while monstruo["vida"] > 0 and vida > 0:
        mostrar_estadisticas(jugador, monstruo)  # Mostrar las estadísticas antes de cada acción
        accion = wn.textinput("Acción", "¿Qué haces? (Atacar o Esquivar)").capitalize()
        
        if accion == "Atacar":
            daño_infligido = random.randint(1, daño)
            monstruo["vida"] -= daño_infligido
            texto.clear()
            texto.write(f"¡Golpeas al {monstruo['nombre']} por {daño_infligido} de daño!", align="center", font=("Courier", 24, "normal"))
            time.sleep(1)
        elif accion == "Esquivar":
            if random.random() < agilidad / 20:
                texto.clear()
                texto.write("¡Esquivaste el ataque!", align="center", font=("Courier", 24, "normal"))
                time.sleep(1)
                continue
            else:
                texto.clear()
                texto.write("¡Fallaste al esquivar!", align="center", font=("Courier", 24, "normal"))
                time.sleep(1)
        else:
            texto.clear()
            texto.write("Acción no válida. Intenta de nuevo.", align="center", font=("Courier", 24, "normal"))
            time.sleep(1)
            continue

        if monstruo["vida"] > 0:
            daño_recibido = random.randint(1, monstruo["daño"])
            vida -= daño_recibido
            texto.clear()
            texto.write(f"El {monstruo['nombre']} te golpea por {daño_recibido} de daño. Vida restante: {vida}", align="center", font=("Courier", 24, "normal"))
            time.sleep(1)