def partition(T, deb, fin, ipivot=None):
    if ipivot is None:
        ipivot = fin
    if ipivot < fin:
        T[ipivot], T[fin] = T[fin], T[ipivot]
        ipivot = fin
    pivot = T[ipivot]

    i = deb
    for j in range(deb, fin-1):
        if T[j] <= pivot:
            T[i], T[j] = T[j], T[i]
            i = i + 1
    T[i], T[fin] = T[fin], T[i]


if __name__ == "__main__":
    T = [3, 6, 5, 3, 5, 6, 1, 7, 0.5, 8, 4]
    partition(T, deb=0, fin=len(T)-1)
    print(T)