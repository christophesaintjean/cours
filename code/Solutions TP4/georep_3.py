import math 
from turtle import *

k = int(input(" k ? "))

for m in range(179, 90, -1):
    if 360*k % m == 0:
        break
print(m)

m = None
for m_ in range(91, 179+1, 1):
    if 360*k % m_ == 0:
        m = m_
print(m)


x0 = xcor()
y0 = ycor()
    
while True:
    forward(100)
    right(m)
    x = xcor()
    y = ycor()
    c_x = math.isclose(x, x0, abs_tol=1e-8)
    c_y = math.isclose(y, y0, abs_tol=1e-8)
    print(x, y, flush=True)
    if c_x and c_y:
        break

exitonclick()

