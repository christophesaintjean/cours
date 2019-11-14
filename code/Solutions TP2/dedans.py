x = float(input("x ?"))

print('*' * 10 + " avec and " + '*'* 10)
if x >= 0 and x<= 1:
    print(x, "est dans [0,1]")
else:
    print(x, "n'est pas dans [0,1]")

print('*' * 10 + " imbriques " + '*'* 10)
if x >= 0:
    if x <= 1:
        print(x, "est dans [0,1]")
    else:
        print(x, "n'est pas dans [0,1],  > 1")
else:
    print(x, "n'est pas dans [0,1],  < 0")

print('*' * 10 + " sans and " + '*'* 10)
if 0 <= x <= 1:
    print(x, "est dans [0,1]")
else:
    print(x, "n'est pas dans [0,1]")


    