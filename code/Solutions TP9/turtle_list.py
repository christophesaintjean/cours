from turtle import *


def rect(x, y, h, l=30):
    penup()
    setposition(x, y)
    pendown()
    forward(l)
    left(90)
    forward(h)
    left(90)
    forward(l)
    left(90)
    forward(h)
    left(90)


setup(1000, 1000)
"""
rect(0, 0, 100, 30)
#
rect(0, 0, 100, 30)
rect(30, 0, 180, 30)
rect(60, 0, 50, 30)
"""

def histo(L, larg, x0=0, y0=0):
    for i, x in enumerate(L):
        rect(x0 + i * larg, y0, x, larg)


clear()
histo([100, 50, -20, 200, 10], 30)