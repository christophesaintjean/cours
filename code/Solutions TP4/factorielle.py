while True:
    n = int(input("Entrez un nombre positif : "))
    if n >= 0:
        break

fact = 1
for i in range(2, n + 1):
    fact = fact * i
print(n, "! = ", fact)
