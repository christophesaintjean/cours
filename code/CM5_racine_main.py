import math


def racine_dicho(x):
    min, max, eps = 0, x, 1e-10
    while True:
        r = (min + max) / 2
        if abs(r * r - x) < eps:
            break
        elif r * r < x:
            min = r
        else:
            max = r
    return r


if __name__ == "__main__":
    x = float(input("x ? "))
    sq_dicho = racine_dicho(x)
    sq_math = math.sqrt(x)
    print(f"La racine carrée de {x} est {sq_dicho} (= {sq_math})")
