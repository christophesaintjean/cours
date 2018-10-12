from turtle import *

while True:
    ordre = input("Entrez un ordre ? ")

    if ordre == "A" or ordre =='a':
        print("Le robot avance de 100 pixels")
        forward(100)
    elif ordre == "R" or ordre =='r':
        print("Le robot recule de 100 pixels")
        backward(100)
    elif ordre == "G" or ordre =='g':
        print("Le robot tourne à gauche de 90 degrés")
        left(90)
    elif ordre == "D" or ordre =='d':
        print("Le robot tourne à droite de 90 degrés")
        right(90)
    elif ordre == "Q" or ordre =='g':
        print("Quitter")
        break
    else:
        print("Le robot ne comprend pas " + ordre + ".")
        
    print("Fin de l'ordre")

exitonclick()
