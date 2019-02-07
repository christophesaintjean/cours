from random import randint


def pivot_premier(T, g, d):
    return g


def pivot_dernier(T, g, d):
    return d


def pivot_milieu(T, g, d):
    return (g + d) // 2


def pivot_median(T, g, d):
    i1, i2, i3 = [randint(g, d) for _ in range(3)]
    if T[i2] <= T[i1] <= T[i3]: return i1
    if T[i3] <= T[i1] <= T[i2]: return i1
    if T[i1] <= T[i2] <= T[i3]: return i2
    if T[i3] <= T[i2] <= T[i1]: return i2
    return i3


def partition(T, g, d, ipivot=None):
    if ipivot is None:
        ipivot = pivot_median(T, g, d)
    if ipivot < d:
        T[ipivot], T[d] = T[d], T[ipivot]
        ipivot = d
    pivot = T[ipivot]

    i = g
    for j in range(g, d):
        if T[j] <= pivot:
            T[i], T[j] = T[j], T[i]
            i = i + 1
    T[i], T[d] = T[d], T[i]
    return i


def trirapide(T, g=0, d=None):
    if d is None:
        d = len(T) - 1
    if g < d:
        ipivot = partition(T, g, d)
        trirapide(T, g, ipivot - 1)
        trirapide(T, ipivot + 1, d)


def trirapide_bis(T):
    if len(T) > 0:
        pivot = T[pivot_median(T, 0, len(T) - 1)]
        Tg = [Ti for Ti in T if Ti < pivot]
        Te = [Ti for Ti in T if Ti == pivot]
        Td = [Ti for Ti in T if Ti > pivot]
        return trirapide_bis(Tg) + Te + trirapide_bis(Td)
    return []


if __name__ == "__main__":
    T = [3, 6, 5, 3, 5, 6, 1, 7, 0.5, 8, 4]
    ipivot = partition(T, g=0, d=len(T) - 1)
    print(T)
    print(ipivot, T[ipivot])

    T = [3, 6, 5, 3, 5, 6, 1, 7, 0.5, 8, 4]
    trirapide(T)
    print(T)

    T = [3, 6, 5, 3, 5, 6, 1, 7, 0.5, 8, 4]
    print(trirapide_bis(T))
