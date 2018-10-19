n = None

while n is None or n < 0:
    n = int(input("Entrez un nombre positif : "))

fact = 1
for i in range(2, n + 1):
    fact = fact * i
print(n, "! = ", fact)
