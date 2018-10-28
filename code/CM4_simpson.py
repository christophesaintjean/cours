Homer = {'age': 39, 'sexe': 'M', 'prénom': 'Homer', 'nom': 'Simpson'}
Marge = {'age': 34, 'sexe': 'F', 'prénom': 'Majorie', 'nom': 'Bouvier', 'surnom': 'marge'}
Lisa = {'age': 8, 'sexe': 'F', 'prénom': 'Lisa', 'nom': 'Simpson'}
Bart = {'age': 10, 'sexe': 'M', 'prénom': 'Bartholomew', 'nom': 'Simpson', 'surnom': 'Bart'}

Homer['enfants'] = [Lisa, Bart]

print(Homer)

for dict_enf in Homer['enfants']:
    print(dict_enf['prénom'])

for dict_enf in Homer['enfants']:
    dict_enf['père'] = Homer

test = Homer is Homer['enfants'][0]['père']
