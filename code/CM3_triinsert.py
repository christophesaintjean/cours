def triinsert(T):
    """
    Version en place
    """
    for i in range(1, len(T)):
        cle = T[i]
        j = i - 1
        while j >= 0 and T[j] > cle:
            T[j+1] = T[j]
            j = j - 1
        T[j+1] = cle
    return T

