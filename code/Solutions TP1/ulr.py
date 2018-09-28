from turtle import *

l=50  # longueur d'un segment élémentaire

# tracé du U
forward(l)
right(90)

forward(4*l)
left(90)

forward(l)
left(90)

forward(4*l)
right(90)

forward(l)
right(90)

forward(5*l)
right(90)

forward(3*l)
right(90)

forward(5*l)

# Déplacement à la position de la lettre suivante
# sans tracer
penup()
right(90)
forward(4*l)
pendown()

# tracé du L
forward(l)
right(90)

forward(4*l)
left(90)

forward(2*l)
right(90)

forward(l)
right(90)

forward(3*l)
right(90)

forward(5*l)

# Déplacement à la position de la lettre suivante
# sans tracer

penup()
right(90)
forward(4*l)
pendown()

## tracé du R
forward(3*l)
right(90)

forward(3*l)
right(90)

forward(l/2)
left(100)

forward(2*l)
right(100)

forward(l)
right(80) # car 100+80 == 180 ...

forward(2*l)
left(80)

forward(l/2)
left(90)

forward(2*l)
right(90)

forward(l)
right(90)
forward(5*l)

# tracé à l'intérieur du R
penup()
right(90)
forward(l)
right(90)
forward(l)

pendown()
forward(l)
left(90)
forward(l)
left(90)
forward(l)

left(90)
forward(l)

done()




