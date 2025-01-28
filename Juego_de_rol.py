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