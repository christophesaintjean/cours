## sélection des noms qui contiennent une voyelle en début ou en fin

voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
noms = ['mila', 'mathis', 'anne', 'myriam', 'eloan', 'pierre', 'jules']

select = []

for nom in noms:
    for voyelle in voyelles:
        if nom[0] == voyelle or nom[-1]==voyelle:
            select.append(nom)
            break

print(select)
