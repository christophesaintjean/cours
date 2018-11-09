

L = [2, -4, 3, 0, -2]
print(L[0], L[-5], L[4], L[-1])

L[1] = 0
L[3] = L[2] + L[4]
print(L)

aux = L[0]
L[0] = L[1]
L[1] = aux
print(L)

print((L[1], L[0]))
(L[0], L[1]) = (L[1], L[0])
print(L)

L.remove(0)
# del L[0]  # n'est pas la même chose
print(L)
