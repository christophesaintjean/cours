def decomposition(n, m):
    a = n // m
    b = n % m
    return {'quotient': a, 'reste': b}