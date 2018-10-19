from turtle import *
k = 10

for m in range(179, 90, -1):
    if 360*k % m == 0:
        break
print(m)

# for _ in range(50):
#     forward(100)
#     left(m)
#
# exitonclick()

while True:
    forward(100)
    right(m)
    x = xcor()
    y = ycor()
    # x, y = position()
    print(x, y, flush=True)
    #if x == 0. and y == 0.:
    if abs(x - 0.) < 1e-6 and abs(y - 0.) < 1e-6:
        break

exitonclick()

