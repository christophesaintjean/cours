
def nb_voyelles(mot):
    voyelles = 'aeiouy'
    cpt = 0
    for lettre in mot:
        if lettre in voyelles:
            cpt = cpt + 1
    return cpt


print("Nombre de voyelles de 'le petit chat est mort'", nb_voyelles('le petit chat est mort'))


def que_des_voyelles(mot):
    voyelles = 'aeiouy'
    for lettre in mot:
        if lettre not in voyelles:
            return False
    return True


def que_des_voyelles2(mot):
    return len(mot) == nb_voyelles(mot)


print("Que des voyelles 'le petit chat est mort'", que_des_voyelles('le petit chat est mort'))
print("Que des voyelles 'le petit chat est mort'", que_des_voyelles('le petit chat est mort'))


def sans_voyelle(chaine, char='*'):
    voyelles = 'aeiouy'
    result = ''
    for lettre in chaine:
        if lettre not in voyelles:
            result = result + lettre
        else:
            result = result + char
    return result


print("Sans voyelle 'le petit chat est mort' : ", sans_voyelle('le petit chat est mort', ''))
print("Sans voyelle 'le petit chat est mort' : ", sans_voyelle('le petit chat est mort'))


def cpt_voyelle(mot):
    dico_cpt = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}
    for lettre in mot:
        if lettre in dico_cpt.keys():
            dico_cpt[lettre] += 1
    return dico_cpt


print("le petit chat est mort", cpt_voyelle('le petit chat est mort'))