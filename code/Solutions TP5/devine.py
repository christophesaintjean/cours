min, max = 1, 20

print("Début du jeu [" + str(min) + "," + str(max) + "]")
print(19 * '-')

while True:
    prop = (min + max) // 2
    estProp = input("Est ce " + str(prop) + " ?  ")
    if estProp == 'True':
        break
    else:
        estPlusGrand = input("Plus grand que " + str(prop) + " ?  ")
        if estPlusGrand == 'True':
            min = prop + 1
        else:
            max = prop - 1
    if min > max:
        print("J'arrete de jouer avec un tricheur !!")
        break

