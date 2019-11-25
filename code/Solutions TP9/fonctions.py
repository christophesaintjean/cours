def aire_carre(cote):
    if cote >= 0:
        aire = cote * cote
    else:
        aire = None
    return aire


def aire_rectangle(long, larg):
    if long >= 0 and larg >= 0:
        return long * larg
    return None


def aire_carre2(cote):
    return aire_rectangle(cote, cote)


cote = float(input("Cote du carré ? "))
print("aire_carre2", aire_carre2(cote))


def aire_rectangle2(long, larg=None):
    if larg is None or long == larg:
        return aire_carre(long)
    return long * larg


cote = float(input("Cote du carré ? "))
aire = aire_carre(cote)
aire2 = aire_carre2(cote)
print(f"L'aire d'un carré de coté {cote} est {aire} (ou {aire2})")

longueur = float(input("Longueur ? "))
largeur = float(input("Largeur ? "))
aire = aire_rectangle(longueur, largeur)
aire2 = aire_rectangle2(longueur, largeur)
aire3 = aire_rectangle2(longueur)

print(f"L'aire d'un rectangle {longueur}x{largeur} est {aire} (ou {aire2} ou {aire3})")


def coords_carre(cote, x0y0=(0, 0)):
    x0, y0 = x0y0
    L = [(x0, y0), (x0 + cote, y0), (x0 + cote, y0 + cote), (x0, y0 + cote)]
    return L


coords_carre(1, (0, 0))
coords_carre(3, (2, 1))
coords_carre(1)
bg, bd, hd, hg = coords_carre(3, (2, 1))
