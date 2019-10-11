n = 1
while n<=5:   # n != 6 ou n < 6
    print(n, end=", ")
    n = n + 1
   
print("\n"*2 + "*" * 15 + "\n")











## Version correcte mais déconseillée
n = 2
while n<=12:
    print(n, end=", ")
    n = n + 2

print("\n"*2 + "*" * 15 + "\n")






n = 2
while n<=12:
    if n % 2 == 0:
        print(n, end=", ")
    n = n + 1

print("\n"*2 + "*" * 15 + "\n")


n = 3
while n<=21:
    if n % 2 == 0:
        print(n, end=", ")
    n = n + 1
print("\n"*2 + "*" * 15 + "\n")


n = 130
cpt_5 = 0
while cpt_5 < 10:
    if n % 5 == 0:
        print(n, end=", ")
        cpt_5 = cpt_5 + 1
    n = n - 1
    
print("\n"*2 + "*" * 15 + "\n")
#  mauvaise façon de faire même si le résultat est correct !
n = 130
while n >= 85:
    print(n, end=", ")
    n = n - 5       

