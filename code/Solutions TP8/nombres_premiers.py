n = 97
N = 35000

# n (= 97) est il premier ?
for i in range(2, n):
    if n % i == 0:
        print("{} n'est pas premier : {}".format(n, i))
        break
else:
    print("{} est premier".format(n))


def est_premier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print("*" * 5 + " Stratégie 1 " + "*" * 5)
P = []
for n in range(2, N + 1):  # les nombres pour lesquels on va tester la primalité
    # print(f"{n}: ", end="")
    for i in range(2, n):
        # print(f"{i}", end=",")
        if n % i == 0:
            # print("--")
            break
    else:
        # print("++")
        P.append(n)

print(f"Il y a {len(P)} nombres premiers entre 2 et {N}")

print("*" * 5 + " Stratégie 2 " + "*" * 5)
P = []
for n in range(2, N + 1):  # les nombres pour lesquels on va tester la primalité
    # print(f"{n}: ", end="")
    for i in P:
        # print(f"{i}", end=",")
        if n % i == 0:
            # print("--")
            break
    else:
        # print("++")
        P.append(n)

print(f"Il y a {len(P)} nombres premiers entre 2 et {N}")

print("*" * 5 + " Stratégie 3 " + "*" * 5)

###   ATTENTION CETTE VERSION NE DEVRAIT PAS MARCHER ET POURTANT ...
L = []
for i in range(2, N + 1):
    L.append(i)

P = []
while L:  # L n'est pas vide
    p = L[0]
    P.append(p)
    for i, Li in enumerate(L):
        if Li % p == 0:
            del L[i]  ###  Regarder au débugger L et i ......
print(f"Il y a {len(P)} nombres premiers entre 2 et {N}")

print("*" * 5 + " Stratégie 3 (autre version) " + "*" * 5)
###   Version propre
L = []
for i in range(2, N + 1):
    L.append(i)

P = []
while L:  # L n'est pas vide
    p = L[0]
    P.append(p)
    L2 = []
    for Li in L:
        if Li % p != 0:     ### on garde que ceux qui ne sont pas multiples de p
            L2.append(Li)
    L = L2
print(f"Il y a {len(P)} nombres premiers entre 2 et {N}")