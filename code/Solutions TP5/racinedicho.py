import math

a = float(input("Calcul de la racine de "))

min, max = 0, a
eps = 1e-10

cpt = 0
while True:
    cpt += 1
    r = (min + max) / 2
    if abs(r*r - a) < eps:
        break
    elif r*r < a:
        min = r
    else:
        max = r
print("La racine de", a, "est", r, "    (", math.sqrt(a), ")")
print("Nombre de propositions : ", cpt)
