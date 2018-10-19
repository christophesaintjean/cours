import random

min, max = 1, 20

print("Début du jeu [" + str(min) + "," + str(max) + "]")
print(19*'-')
x = random.randint(min, max)
print("Valeur à deviner : ", x)
cpt = 0
while True:
    cpt += 1
    # Stratégie optimale : la dichotomie
    prop = (min + max) // 2
    # Une autre stratégie moins bonne ...
    # prop = random.randint(min, max)
    # Une autre stratégie carrément mauvaise
    # prop = min
    print('Proposition', prop)
    estProp = x == prop
    print("Est ce " + str(prop) + " ?  " + str(estProp))
    if estProp:
        break
    else:
        estPlusGrand = x > prop
        print("Est plus grand que " + str(prop) + " ?  " + str(estPlusGrand))
        if estPlusGrand:
            min = prop + 1
        else:
            max = prop - 1
print("Nombre de propositions : ", cpt)
