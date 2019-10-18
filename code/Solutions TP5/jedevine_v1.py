import random

min, max = 1, 100
print("Début du jeu [" + str(min) + "," + str(max) + "]")
print(19*'-')
x = random.randint(min, max)
prop = None

cpt = 0
while True:
    prop = int(input("Propose un nombre: "))
    cpt = cpt + 1
    if x < prop:
        print("Plus petit.")
    elif x > prop:
        print("Plus grand.")
    else:
        break

print("Bravo, j'avais choisi " + str(prop) + ".")
print("en " + str(cpt) + " coups.")