from temperature import *

temp = 100
print(f"{temp} degrés Celsuis font {deCversF(temp)} degrés Fahrenheit")

with open('celsius.txt', 'r') as fc:
    with open('fahrenheit.txt', 'w+') as ff:
        while True:
            ligne = fc.readline()
            if ligne:
                tc = float(ligne)
                print(deCversF(tc), file=ff)
            else:
                break