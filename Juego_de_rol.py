import turtle
import time
import random

# Configuración del texto
t = turtle.Turtle()
t.color("white")
t.hideturtle()
t.penup()
t.speed(0)

def print_banner():
    banner = [
        " ██████╗ ██████╗  ██████╗      ██████╗  █████╗ ███╗   ███╗███████╗",
        " ██╔══██╗██╔══██╗██╔═══██╗     ██╔══██╗██╔══██╗████╗ ████║██╔════╝",
        " ██████╔╝██████╔╝██║   ██║     ██║  ██║███████║██╔████╔██║███████╗",
        " ██╔═══╝ ██╔═══╝ ██║   ██║     ██║  ██║██╔══██║██║╚██╔╝██║╚════██║",
        " ██║     ██║     ╚██████╔╝     ██████╔╝██║  ██║██║ ╚═╝ ██║███████║",
        " ╚═╝     ╚═╝      ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝"
    ]
    y_start = 250
    for line in banner:
        t.goto(0, y_start)
        t.write(line, align="center", font=("Courier", 16, "normal"))
        y_start -= 30

print_banner()

# Configuración de la pantalla
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("⚔️ RPG Game ⚔️")

t.goto(0, 200)  # Centrando mensajes

victorias = 0
vida = 0
vidatotal = 0
daño = 0
agilidad = 0
inteligencia = 0

def seleccionar_clase():
    global vida, vidatotal, daño, agilidad, inteligencia
    clases = {
        "Mago": (1, 10, 1, 10, 10, 20),
        "Guerrero": (10, 20, 10, 20, 1, 10),
        "Pícaro": (5, 15, 5, 15, 5, 15)
    }
    while True:
        clase = wn.textinput("Seleccionar Clase", "Elige una clase: Mago, Guerrero o Pícaro").capitalize()
        if clase in clases:
            rangos = clases[clase]
            vida = random.randint(rangos[0], rangos[1])
            daño = random.randint(rangos[2], rangos[3])
            agilidad = random.randint(rangos[4], rangos[5])
            inteligencia = random.randint(rangos[4], rangos[5])
            vidatotal = vida
            return clase
        else:
            t.clear()
            t.write("Clase no válida. Intenta de nuevo.", align="center", font=("Courier", 24, "normal"))
            time.sleep(2)
            t.clear()

def generar_monstruo():
    return {
        "nombre": random.choice(["☠️ Esqueleto ☠️", "🧟 Zombi 🧟", "👹 Orco 👹", "🐉 Dragón 🐉"]),
        "vida": random.randint(5, 20),
        "daño": random.randint(1, 10)
    }

def mostrar_estadisticas(jugador, monstruo):
    t.clear()
    t.goto(0, 100)
    t.write(f"❤ Vida: {vida} | ⚔️ Daño: {daño} | 🏃 Agilidad: {agilidad} | 📖 Inteligencia: {inteligencia}", align="center", font=("Courier", 18, "normal"))
    t.goto(0, 50)
    t.write(f"{monstruo['nombre']} | ❤️ Vida: {monstruo['vida']} | 🗡️ Daño: {monstruo['daño']}", align="center", font=("Courier", 18, "normal"))
    time.sleep(2)

def combatir(jugador, monstruo):
    global vida, victorias
    t.clear()
    t.goto(0, 100)
    t.write(f"¡Un {monstruo['nombre']} aparece con {monstruo['vida']} de vida!", align="center", font=("Courier", 24, "normal"))
    time.sleep(2)
    while monstruo["vida"] > 0 and vida > 0:
        mostrar_estadisticas(jugador, monstruo)
        accion = wn.textinput("Acción", "¿Qué haces? (Atacar o Esquivar)").capitalize()
        if accion == "Atacar":
            daño_infligido = random.randint(1, daño)
            monstruo["vida"] -= daño_infligido
            t.clear()
            t.write(f"¡Golpeas al {monstruo['nombre']} por {daño_infligido} de daño!", align="center", font=("Courier", 24, "normal"))
            time.sleep(1)
        elif accion == "Esquivar":
            if random.random() < agilidad / 20:
                t.clear()
                t.write("¡Esquivaste el ataque!", align="center", font=("Courier", 24, "normal"))
                time.sleep(1)
                continue
            else:
                t.clear()
                t.write("¡Fallaste al esquivar!", align="center", font=("Courier", 24, "normal"))
                time.sleep(1)
        else:
            t.clear()
            t.write("Acción no válida. Intenta de nuevo.", align="center", font=("Courier", 24, "normal"))
            time.sleep(1)
            continue
        if monstruo["vida"] > 0:
            daño_recibido = random.randint(1, monstruo["daño"])
            vida -= daño_recibido
            t.clear()
            t.write(f"El {monstruo['nombre']} te golpea por {daño_recibido} de daño. Vida restante: {vida}", align="center", font=("Courier", 24, "normal"))
            time.sleep(1)
    if vida > 0:
        t.clear()
        t.write(f"🏆 ¡Derrotaste al {monstruo['nombre']}!", align="center", font=("Courier", 24, "normal"))
        victorias += 1
        time.sleep(2)
    else:
        t.clear()
        t.write(f"☠️ ¡Has sido derrotado después de {victorias} victorias!", align="center", font=("Courier", 24, "normal"))
        time.sleep(2)
        wn.bye()

clase_jugador = seleccionar_clase()
t.clear()
t.goto(0, 100)
t.write(f"⚔️ Eres un {clase_jugador} listo para la batalla. ¡Prepárate!", align="center", font=("Courier", 24, "normal"))
time.sleep(2)
monstruo_inicial = generar_monstruo()
combatir(None, monstruo_inicial)
