from time import time
from random import randint, seed

def triselect(T):
    """
    Version en place
    """
    for i in range(len(T)-1):
        imin = i
        for j in range(i+1, len(T)):
            if T[j] < T[imin]:
                imin = j
        if imin != i:
            T[i], T[imin] = T[imin], T[i]
    return T


def triselect2(T):
    """
    Autre version
    """
    res = []
    while len(T) > 1:
        imin = 0
        for i in range(1, len(T)):
            if T[i] < T[imin]:
                imin = i
        res.append(T[imin])
        del T[imin]
    return res


seed(13)
## Verification
T = [randint(1, 100) for _ in range(10)]
print(T)
triselect(T)
print(T)

seed(13)
T = [randint(1, 100) for _ in range(10)]
print(T)
T2 = triselect(T)
print(T2)

seed(13)
T = [randint(1, 100) for _ in range(30000)]
debut = time()
triselect(T)
fin = time()
print("Durée (tri par selection en place): ", fin - debut)

seed(13)
T = [randint(1, 100) for _ in range(30000)]
debut = time()
T2 = triselect2(T)
fin = time()
print("Durée (tri par selection version 2): ", fin - debut)