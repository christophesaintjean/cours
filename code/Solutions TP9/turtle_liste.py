from turtle import *

"""
from turtle import penup, pendown, setposition
from turtle import forward, left
from turtle import exitonclick
"""


def rect(h, l, x=0, y=0):
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


"""
rect(100, 20)
rect(50, 20, 20, 0)
rect(120, 20, 40, 0)
hideturtle()
exitonclick()
"""


def histo(H, l=20, x0=0, y0=0):
    x = 0
    for h in H:
        print(x0 + x, y0)
        rect(h, l, x0+x, y0)
        x = x + l


def histo2(H, l=20, x0=0, y0=0):
    for i, h in enumerate(H):
        rect(h, l, x0+i*l, y0)

L = [100, 50, 120, 12, -30, 60, 250, 100]
print(L)
histo2(L, 40, -200, -200)
hideturtle()
exitonclick()