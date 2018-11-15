def f(x):
    return x ** 2


def mon_map(L, fun):
    res = []
    for l in L:
        res.append(fun(l))
    return res


L = [1, 0, 3, 2, -3]
print(mon_map(L, f))
