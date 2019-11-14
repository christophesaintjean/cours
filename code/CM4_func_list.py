
def mult_2(L):
    L2 = []
    for el in L:
        L2.append(2*el)
    return L2

def mult_2_bis(L):
    for i, el in enumerate(L):
        L[i] = 2 * el
    return L

liste = [2, 9, -2, 4]

liste_2 = mult_2(liste)
print(liste_2)

liste_2_bis = mult_2_bis(liste)
print(liste_2_bis)

    
    