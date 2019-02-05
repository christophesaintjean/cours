from time import time
from random import randint, seed
from utils import estTrie

from CM4_trifusion import trifusion, trifusion_bis

seed(13)
T = [randint(1, 100) for _ in range(10)]
print(T)
trifusion(T)
print(T)

seed(13)
T = [randint(1, 100) for _ in range(3000)]
print("Le tableau résultat est trié:", estTrie(trifusion(T)))

seed(13)
T = [randint(1, 100) for _ in range(3000000)]
debut = time()
trifusion(T)
fin = time()
print("Durée (tri fusion: ", fin - debut)

seed(13)
T = [randint(1, 100) for _ in range(10)]
print(T)
trifusion_bis(T)
print(T)

seed(13)
T = [randint(1, 100) for _ in range(3000)]
trifusion_bis(T)
print("Le tableau résultat est trié:", estTrie(T))

seed(13)
T = [randint(1, 100) for _ in range(3000000)]
debut = time()
trifusion_bis(T)
fin = time()
print("Durée (tri fusion: ", fin - debut)
