import math

x = input("x ? ")
x = float(x)
# x = float(input("x ? "))

# attention aux :
if x >= 0:
    # Si x>=0
    # indentation obligatoire !!!
    print("La racine carrée de", x, "est", math.sqrt(x))
else:
    # Si x<0
    print("Impossible de calculer la racine de", x)
