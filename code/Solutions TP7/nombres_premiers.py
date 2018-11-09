# Test de primalité de n

n = 97
premier = True
for i in range(2, n):
    if n % i == 0:
        print(i)
        premier = False
        break
if premier:
    print(n, "est premier")
else:
    print(n, "n'est pas premier")

# Liste des nombres premiers inférieurs à 1000
n_max = 1000
P = []
for n in range(2, n_max+1):
    premier = True
    for i in range(2, n):
        if n % i == 0:
            premier = False
            break
    if premier:
        P.append(n)

print("Liste des nombres premiers")
print(P)
print("Il y a", len(P), "nombres premiers inférieurs à", n_max)


# deuxième version plus rapide (tester n_max= 20000)
P = []
for n in range(2, n_max+1):
    premier = True
    for i in P:
        if n % i == 0:
            premier = False
            break
    if premier:
        P.append(n)

print("Liste des nombres premiers")
print(P)
print("Il y a", len(P), "nombres premiers inférieurs à", n_max)