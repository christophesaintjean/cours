import math
from racine import racine_dicho

x = float(input('x ? '))
if abs(math.sqrt(x) - racine_dicho(x)) < 1e-6:
    print("Les valeurs sont les mêmes")
else:
    print("Roger, on a un problème !!!")
