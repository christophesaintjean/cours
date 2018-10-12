#x = 1
#while x <=5:
#    print(x, end=' ')
#    x = x + 1

for x in range(1, 5+1, 1):
    print(x, end=' ')
    
print()

for x in range(5):
    print(x+1, end=' ')

print()

a = int(input(" a  ?  "))
b = int(input(" b  ?  "))

prodab = 0
for c in range(b):
    prodab = prodab + a

print(prodab)
