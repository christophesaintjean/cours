def estpair(n):
    return n % 2 == 0

print(estpair(7))

def estdiv(a, b):
    return a % b == 0


print(estdiv(7, 3))


def estpair2(n):
    return estdiv(n, 2)


def estpremier(n):
    for i in range(2, n):
        if estdiv(n, i):
            return False
    return True


n_max = 1000
P = []
for n in range(2, n_max+1):
    if estpremier(n):
        P.append(n)
print(P)


def estpair(n):
    return n % 2 == 0


# print(estpair(6))

def estdiv(a, b):
    return a % b == 0


# print(estdiv(5, 2))

def estpair2(n):
    return estdiv(n, 2)


# print(estpair2(11))

def estpremier(n):
    """Teste si un nombre entier strictement positif est premier."""
    for i in range(2, n):
        if estdiv(n, i):
            return False
    return True


print(estpremier(102))

L = []  # liste des nombres premiers
n = 2
while len(L) < 1000:
    if estpremier(n):
        L.append(n)
    i = i + 1


def estdiv(a, b=2):
    return a % b == 0

