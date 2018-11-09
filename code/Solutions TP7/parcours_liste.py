import random

R = []
for _ in range(10):
    alea = random.randint(1, 20)
    R.append(alea)
print(R)

long = len(R)

for i in range(long):
    print(R[i], end=':')
print()

for ri in R:
    print(ri, end=':')
print()

somme = 0
for ri in R:
    somme = somme + ri
print("La somme des éléments est", somme)

irmax, rmax = 0, R[0]
for i in range(long):
    if R[i] > rmax:
        irmax, rmax = i, R[i]
print("La valeur maximum est", rmax, "en position", irmax)

# ou par enumerate
irmax, rmax = 0, R[0]
for i, ri in enumerate(R):
    if ri > rmax:
        irmax, rmax = i, ri
print("La valeur maximum est", rmax, "en position", irmax)

cpt = 0
for ri in R:
    if ri >= 10:
        cpt += 1
print("Il y a", cpt, "sup. à 10")

R2 = []
for ri in R:
    if ri > 10:
        R2.append(-ri)
    else:
        R2.append(ri)
print(R2)

R3 = R + R2
print(R3)



