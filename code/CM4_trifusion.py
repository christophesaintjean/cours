def trifusion(T):
    if len(T) > 1:
        mil = len(T) // 2

        # attention mémoire ici
        G, D = T[:mil], T[mil:]

        trifusion(G)
        trifusion(D)

        # Fusion
        i, j, k = 0, 0, 0
        while i < len(G) and j < len(D):
            if G[i] < D[j]:  # On cherche le + petit
                T[k] = G[i]  # il est dans G
                i += 1
            else:
                T[k] = D[j]  # il est dans D
                j += 1
            k += 1

        while i < len(G):  # On termine G
            T[k] = G[i]
            i += 1
            k += 1

        while j < len(D):  # On termine D
            T[k] = D[j]
            j += 1
            k += 1
    return T


def trifusion_bis(T, g=0, d=None, m=None):
    if d is None:
        d = len(T)-1
    if m is None:   # premier appel
        m = max(T) + 1

    if g < d:         # au moins 2 éléments
        mil = (g + d) // 2
        trifusion_bis(T, g, mil, m)
        trifusion_bis(T, mil+1, d, m)

        # Fusion
        i, j = g, mil+1
        k = i
        while i <= mil and j <= d:
            if (T[i] % m) < (T[j] % m):  # On cherche le + petit
                T[k] = T[k] + (T[i] % m) * m
                i += 1
            else:
                T[k] = T[k] + (T[j] % m) * m
                j += 1
            k += 1

        while i <= mil:
            T[k] = T[k] + (T[i] % m) * m
            i += 1
            k += 1

        while j <= d:
            T[k] = T[k] + (T[j] % m) * m
            j += 1
            k += 1

        #  Cout supp.: Recomposer les valeurs
        for k in range(g, d+1):
            T[k] = T[k] // m

