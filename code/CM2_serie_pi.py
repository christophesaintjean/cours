import math

n = 10**6      # n très grand pour simuler l'infini...
som = 0

for k in range(n+1):
    som += (-1)**k / (2*k+1)

print("Approximation de l'algorithme :", 4*som)
print("Valeur système de pi", math.pi)
