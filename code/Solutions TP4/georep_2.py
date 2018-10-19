from turtle import *

speed(1)

n = int(input("Nombre de cotés ? "))
angle = 360 / n
longueur = 1

for i in range(n):
    forward(longueur)
    left(angle)

exitonclick()
