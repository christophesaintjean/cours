from turtle import *

vitesse = int(input("Vitesse ? "))
speed(vitesse)

long = input("Longueur du coté ? ")
if long:
    long = int(long)
else:
    long = 100

sens = input("Sens horaire ? ")
if sens == "True":
    sens = True
elif sens == "False":     # pourquoi est on obligé ?
    sens = False
else:
    quit()
    

#################################

forward(long)

if sens:
    right(120)
else:
    left(120)

forward(long)

if sens:
    right(120)
else:
    left(120)

forward(long)

exitonclick()
