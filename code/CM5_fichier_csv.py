import csv

fichier_telechargement = "titanic.csv"

## Lecture
with open(fichier_telechargement, newline='') as f:
    lecteur = csv.reader(f, delimiter=',', quotechar='"')
    for ligne in lecteur:
        print(ligne)

## Lecture d'un seul trait
with open(fichier_telechargement, newline='') as f:
    lecteur = csv.reader(f, delimiter=',', quotechar='"')
    lignes = list(lecteur)

print(lignes)

## Ecriture
with open('sortie.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lignes)