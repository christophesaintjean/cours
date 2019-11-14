def racine_dicho(x):
    min, max, eps = 0, x, 1e-6
    while True:
        r = (min + max) / 2
        if abs(r * r - x) < eps:
            break
        elif r * r < x:
            min = r
        else:
            max = r
    return r
