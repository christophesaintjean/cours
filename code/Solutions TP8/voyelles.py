m = "le nombre de voyelles est"
m2 = "aueiooyuue"
L = ["une", "histoire", "avec", "des", "listes", ",", "des", "dicos", "et", "des", "chaines"]

voy = "aeiouyAEIOUY"

#Lvoy = ["a", "e", ...]
Lvoy = []
for v in voy:
    Lvoy.append(v)
print(Lvoy)

cpt = 0
for lettre in m:
    if lettre in voy:    # in Lvoy aussi
        cpt = cpt + 1

print(f"{m} {cpt} dans '{m}'")


for lettre in m2:
    if lettre not in voy:
        print("Il n'y a pas que des voyelles: "+ lettre)
        break
else:
    print(f"Il y a que des voyelles dans '{m2}'")

### importante remarque les chaines de caractères sont immutables (non modifiables)
# a = 'abc'
# a[1] = 'E'      # impossible

print("Remplacement des voyelles: ", end="")
m_sansvoy = ""
for l in m:
    if l in voy:
        m_sansvoy = m_sansvoy + "*"
    else:
        m_sansvoy = m_sansvoy + l
print(m_sansvoy)

Lc, Lv = [], []
for ch in L:
    if ch[0] in voy:
        Lv.append(ch)
    else:
        Lc.append(ch)

print(Lv, Lc)

for i in range(len(L)-1):
    if L[i] > L[i+1]:
        print("L n'est pas triée")
        break
else:
    print("L est triée")

#################   Dictionnaires ###############

D = {}
for v in voy:
    D[v] = 0

for l in m:
    if l in voy:
        D[l] = D[l] + 1
"""
for l in m:
    if l in D:       #   On teste que la clé est dans le dico,  c'est donc une voyelle !
        D[l] = D[l] + 1
"""
print(D)

Dcv = {"Lc" : [], "Lv": []}
for ch in L:
    if ch[0] in voy:
        Dcv["Lv"].append(ch)
    else:
        Dcv["Lc"].append(ch)


print(Dcv.keys())
print(Dcv.values())

for k, v in Dcv.items():
    print(f"{k}: {v}")