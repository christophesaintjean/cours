# Nettoie un dictionnaire en eliminant toutes les cles dont la valeur est None


def clean_dict(D):
    for cle, valeur in D.items():
        if valeur is None:
            del D[cle]
    return D
        
def clean_dict_bis(D):
    for cle, valeur in D.copy().items():
        if valeur is None:
            del D[cle]
    return D

def clean_dict_ter(D):
    D2 = {}
    for cle, valeur in D.items():
        if valeur is not None:
            D2[cle] = valeur
    return D2

toto = {'a': 2, 'b': None, 'c': None, 'd': 4}

print(clean_dict_ter(toto))



