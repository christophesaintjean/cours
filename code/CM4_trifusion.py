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

