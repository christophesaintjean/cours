dico = []
with open('dico.txt', 'r') as f:
    for ligne in f:
        dico.append(ligne.rstrip('\n'))

N2L = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
      "6": "mno", "7": "pqrs", "8":"tuv", "9":"wxyz"}

L2N = {}
for N, Ls in N2L.items():
    for L in Ls:
        L2N[L] = N

# Chiffrage Lettre vers Nombres

mot = input("Mot: ")

code = ""
for lettre in mot:
    code = code + L2N[lettre]

print(code)

# Chiffrage Lettre vers Nombres


code = input("Code: ")

dico2 = [mot for mot in dico if len(mot) == len(code)]
print("Etape 0 : reste ", len(dico2), "mots")
for i, n in enumerate(code):
    dico2 = [mot for mot in dico2 if mot[i] in N2L[code[i]]]
    print("Etape", i+1, ": reste ", len(dico2), "mots")
    if len(dico2) < 10:
        print(dico2)

dico2 = dico.copy()
i = 0
while True:
    codei = input()
    if codei == "0":
        break
    dico2 = [mot for mot in dico2 if len(mot)>= i+1 and mot[i] in N2L[codei]]
    print("Etape", i + 1, ": reste ", len(dico2), "mots")
    if len(dico2) < 10:
        print(dico2)
    i = i + 1
