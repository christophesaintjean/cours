# -*- coding: utf-8 -*
import random
from time import time
from CM5_trirapide import partition


def quick_select_rec(T, k):
    if k < 0 or k > len(T)-1:
        return None
    return quick_select_rec_aux(T, k, 0, len(T)-1)


def quick_select_rec_aux(T, k, g, d):
    i_pivot = partition(T, g, d)
    if i_pivot == k:
        return T[i_pivot]
    elif k < i_pivot:
        return quick_select_rec_aux(T, k, g, i_pivot-1)
    else:
        return quick_select_rec_aux(T, k, i_pivot + 1, d)


def quick_select(T, k):
    if k < 0 or k > len(T)-1:
        return None
    g, d = 0, len(T) - 1
    while True:
        i_pivot = partition(T, g, d)
        if i_pivot == k:
            return T[i_pivot]
        elif k < i_pivot:
            d = i_pivot - 1
        else:
            g = i_pivot + 1


def count_select(T, k):
    if k < 0 or k > len(T)-1:
        return None
    m, M = min(T), max(T)
    C = [0] * (M - m + 1)
    for e in T:
        C[e-m] += 1
    i, j = 0, 0
    while j < k + 1:
        if C[i] > 0:
            C[i] -= 1
            j += 1
        else:
            i += 1
    return m+i


if __name__ == "__main__":
    T = [3, 6, 4, 1, -3, 4, 10, -8]
    print(T)
    print(sorted(T))
    print('-'*30)

    for k in range(8):
        T = [3, 6, 4, 1, -3, 4, 10, -8]
        print(quick_select_rec(T, k), T)

    print('-' * 30)
    for k in range(8):
        T = [3, 6, 4, 1, -3, 4, 10, -8]
        print(quick_select(T, k), T)

    print('-' * 30)
    for k in range(8):
        T = [3, 6, 4, 1, -3, 4, 10, -8]
        print(count_select(T, k), T)     # T inchangé
