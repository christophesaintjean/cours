## Lecture

# Lecture de tout en 1 instruction
with open('alice.txt', mode='r') as f:
    lignes = f.readlines()

print(lignes[:9])

# Lecture ligne par ligne

with open('alice.txt', mode='r') as f:
    while True:
        ligne = f.readline()
        if ligne != '':
            print(ligne, end='')
        else:
            break   ## c'est la fin du fichier

# Découpage d'une ligne
une_ligne = lignes[8]
print(une_ligne)
print(une_ligne.split(' '))

## Ecriture
L = [['Hauteur', 'Largeur', 'x0', 'y0'],
     [1, 20, 4, 0],
     [12, 5, 3, -2]]

with open('L.txt', mode='w') as f:
    for l in L:
        print(l, file=f)