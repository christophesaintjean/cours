from turtle import *

"""
for i in range(4):    # range(0, 4, 1)
    forward(100)
    left(90)
"""
n = int(input("n ? "))

for i in range(n):    # range(0, n, 1)
    forward(80)
    left(360/n)


 
exitonclick()

