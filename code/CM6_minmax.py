# -*- coding: utf-8 -*

import itertools
import random
from time import time

def minmax_4(T):
    min = max = T[0]
    for e in T[1:]:
        if e < min:
            min = e
        if e > max:
            max = e
    return min, max

def minmax_3(T):
    if len(T) == 0:
        return None, None
    elif len(T) == 1:
        return T[0], T[0]
    elif len(T) == 2:
        if T[0] < T[1]:
            return T[0], T[1]
        else:
            return T[1], T[0]
    # len(T) >= 3
    min = max = T[0]
    i = 1
    while i + 1 <= len(T) - 1:
        if T[i] < T[i+1]:   # T[i] < T[i+1]
            if T[i] < min:
                min = T[i]
            if T[i+1] > max:
                max = T[i+1]
        else:               # T[i] >= T[i+1]
            if T[i+1] < min:
                min = T[i+1]
            if T[i] > max:
                max = T[i]
        i = i + 2
    if i == len(T) - 1:     # le dernier si n est impair
        if T[-1] < min:
            min = T[-1]
        if T[-1] > max:
            max = T[-1]
    return min, max


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def minmax_3_bis(T):
    if len(T) == 0:
        return None, None
    elif len(T) == 1:
        return T[0], T[0]
    elif len(T) == 2:
        if T[0] < T[1]:
            return T[0], T[1]
        else:
            return T[1], T[0]
    # len(T) >= 3
    min = max = T[0]
    for Ti, Tip1 in grouper(T, 2, min):
        if Ti < Tip1:   # T[i] < T[i+1]
            if Ti < min:
                min = Ti
            if Tip1 > max:
                max = Tip1
        else:               # T[i] >= T[i+1]
            if Tip1 < min:
                min = Tip1
            if Ti > max:
                max = Ti
    return min, max


def minmax_rec_aux(T, g, d):
    if g == d:                 # 1 élément
        return T[g], T[g]
    if g == d + 1:             # 2 éléments
        if T[g] < T[d]:
            return T[g], T[d]
        else:
            return T[d], T[g]
    m = (g + d) // 2
    min_g, max_g = minmax_rec_aux(T, g, m)
    min_d, max_d = minmax_rec_aux(T, m+1, d)

    min = min_g if min_g < min_d else min_d
    max = max_g if max_g > max_d else max_d
    return min, max


def minmax_rec(T):
    return minmax_rec_aux(T, 0, len(T)-1)


def deuxieme(T):
    if len(T) == 1:
        return None
    if len(T) >= 2:
        first, sec = (T[0], T[1]) if T[0] < T[1] else (T[1], T[0])
    for e in T[2:]:
        if e < sec:
            if e < first:
                first, sec = e, first
            else:
                sec = e
    return sec


if __name__ == "__main__":
    T = [3, 6, 4, 1, -3, 4, 10, -8]
    print(minmax_4(T))
    print(minmax_3(T))
    print(minmax_3_bis(T))
    print(minmax_rec(T))

    print(deuxieme(T))
    T = [random.random() for _ in range(3000000)]

    debut = time()
    minmax_4(T)
    fin = time()
    print("Durée: ", fin - debut)

    debut = time()
    minmax_3(T)
    fin = time()
    print("Durée: ", fin - debut)

    debut = time()
    minmax_3_bis(T)
    fin = time()
    print("Durée: ", fin - debut)

    debut = time()
    minmax_rec(T)
    fin = time()
    print("Durée: ", fin - debut)

    debut = time()
    min(T), max(T)
    fin = time()
    print("Durée: ", fin - debut)

