x = input("x ? ")
x = float(x)

if x >= 0 and x <= 1:
    print("x est dans l'intervalle [0,1]")
else:
    print("x n'est pas dans l'intervalle [0,1]")

# autre version spécifique à Python

if 0 <= x <= 1:
    print("x est dans l'intervalle [0,1]")
else:
    print("x n'est pas dans l'intervalle [0,1]")
