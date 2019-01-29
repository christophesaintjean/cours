from time import time
from random import randint, seed
from utils import estTrie

from CM4_trifusion import trifusion

seed(13)
T = [randint(1, 100) for _ in range(10)]
print(T)
trifusion(T)
print(T)

# seed(13)
# T = [randint(1, 100) for _ in range(3000)]
# print("Le tableau résultat est trié:", estTrie(trifusion(T)))
#
# seed(13)
# T = [randint(1, 100) for _ in range(30000)]
# debut = time()
# trifusion(T)
# fin = time()
# print("Durée (tri fusion: ", fin - debut)
