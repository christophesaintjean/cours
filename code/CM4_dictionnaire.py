## sélection des noms qui contiennent une voyelle en début ou en fin

alphabet ='abcdefghijklmnopqrstuvwxyz'
texte = 'le petit chat est mort'
dico_cpt = {}  # également dico_cpt = dict()

for lettre in texte:
    if lettre not in alphabet:
        pass     # on fait rien
    elif lettre not in dico_cpt.keys():
        dico_cpt[lettre] = 1
    else:
        dico_cpt[lettre] += 1

print("Dans l'ordre d'insertion du dico")
for lettre, nb in dico_cpt.items():
    print(lettre, " : ", nb)

print("Dans l'ordre alphabétique")

for lettre in alphabet:
    if lettre in dico_cpt.keys():
        print(lettre, " : ", dico_cpt[lettre])


