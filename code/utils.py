def estTrie(L, deb=0, fin=None):
    if fin is None:
        fin = len(L)
    for i in range(fin-1):
        if L[i] > L[i+1]:
            return False
    return True

