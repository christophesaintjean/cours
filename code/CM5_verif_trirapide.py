from time import time
from random import randint, seed
from utils import estTrie

from CM5_trirapide import trirapide

seed(13)
T = [randint(1, 100) for _ in range(10)]
print(T)
trirapide(T)
print(T)

seed(13)
T = [randint(1, 100) for _ in range(3000)]
trirapide(T)
print("Le tableau résultat est trié:", estTrie(T))

# seed(13)
# T = [randint(1, 100) for _ in range(3000000)]
# debut = time()
# trirapide(T)
# fin = time()
# print("Durée tri rapide: ", fin - debut)

