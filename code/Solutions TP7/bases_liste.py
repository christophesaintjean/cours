L = [4, -3, 0, 6, 8]

print(L[0])
print(L[4], L[-1])

L[1] = 0
L[3] = L[2] + L[4]
print(L)

aux = L[0]
L[0] = L[1]
L[1] = aux
print(L)

L[0], L[1] = L[1], L[0]
print(L)

L[:2] = L[1], L[0]
print(L)

L[:2] = L[:2][::-1]
print(L)

L.remove(0)
print(L)
