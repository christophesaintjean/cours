import math

n = 100
som = 0

for k in range(n+1):
    som = som + (-3)**-k / (2*k+1)

print("Approximation de l'algorithme :", math.sqrt(12) * som)
print("Valeur système de pi", math.pi)

print('-'*10 + ' Recherche de la meilleure série ' + '-'*10)

print("Serie 2 (TP)")
erreur = 1e-8

som = 0
k = 0
approx_pi = 0
python_pi = math.pi

while abs(approx_pi - python_pi) >= erreur:
    som = som + (-3) ** -k / (2 * k + 1)
    approx_pi = math.sqrt(12) * som
    k = k + 1
print(k, 'termes suffisent pour une approximation à',
      erreur, 'près!')

print("Serie 1 (cours)")
som = 0
k = 0
approx_pi = 0

while abs(approx_pi - python_pi) >= erreur:
    som = som + (-1) ** k / (2 * k + 1)
    approx_pi = 4 * som
    k = k + 1
print(k, 'termes suffisent pour une approximation à',
      erreur, 'près!')
