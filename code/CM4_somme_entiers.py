def somme_n_entiers(n):
    som = 0
    for i in range(1, n+1):
        som += i
    return som

m = somme_n_entiers(10)
print(m)