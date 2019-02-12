from time import time
from random import randint


def RechDico(T, x):
    g, d = 0, len(T) - 1
    while g <= d:
        mil = (g + d) // 2
        if T[mil] == x:
            return mil
        if x < T[mil]:
            d = mil - 1
        else:
            g = mil + 1
    return None


def RechInterp(T, x):
    g, d = 0, len(T) - 1
    if x < T[0] or x > T[-1]:
        return False
    while g < d:
        a = (T[d] - T[g]) / (d - g)
        if a == 0:  # Valeurs constantes dans T[g..d]
            return x == T[g]
        #b = T[g] - a * g
        #i_x = (x - b) / a
        i_x = (x - T[g]) / a + g
        i_x = int(round(i_x))
        if T[i_x] == x:
            return i_x
        elif x < T[i_x]:
            d = i_x - 1
        else:
            g = i_x + 1
    if T[g] == x:  # g = d
        return g
    return None


if __name__ == "__main__":
    n = 3000000
    m = 50
    #T = sorted([randint(1, 100000) for _ in range(n)])
    T = list(range(10**9))
    X = [randint(0, n - 1) for _ in range(m)]

    debut = time()
    for x in X:
        RechDico(T, x)
    fin = time()
    print("Dicho: ", fin - debut)

    debut = time()
    for x in X:
        RechInterp(T, x)
    fin = time()
    print("Interp: ", fin - debut)
