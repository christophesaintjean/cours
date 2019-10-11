# n = 1
# while n<=5:   # n != 6 ou n < 6
#    print(n, end=", ")
#    n = n + 1

for n in range(1, 5+1, 1):      # attention [start, stop[
    print(n, end=", ")
    
 
print()

a = int(input("a ? "))
b = int(input("b ? "))

produit_ab = 0

if b < a:
    for i in range(0, b):    # ou range(b) ou range(1, b+1)
        produit_ab = produit_ab + a
else:
    for i in range(0, a):
        produit_ab = produit_ab + b
        
assert (produit_ab == a*b)
print("{} * {} = {}".format(a, b, produit_ab))
    