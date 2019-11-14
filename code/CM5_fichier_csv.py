import csv

fichier_telechargement = "stationnement.csv"

## Lecture
with open(fichier_telechargement, 'r', newline='') as f:
    lecteur = csv.reader(f, delimiter=',', quotechar='"')
    # next(lecteur)       # on ne lit pas l'entete
    lignes = []
    for ligne in lecteur:
        lignes.append(ligne)
        print(ligne)

print('\n'*2)
## Lecture d'un seul trait
with open(fichier_telechargement, 'r', newline='') as f:
    lecteur = csv.reader(f, delimiter=',', quotechar='"')
    # next(lecteur)
    lignes = list(lecteur)
    print(lignes)


## Ecriture
with open('sortie.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lignes)