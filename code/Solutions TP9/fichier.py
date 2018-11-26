from temperature import deCversF


# de C vers F
# tc = input("Saisissez la température en degrés Celsius : ")
# tc = float(tc)
#
# tf = deCversF(tc)
# print(tf, "degrés Farenheit")

F = []
with open('celsius.txt', 'r') as lecture:
    for line in lecture:
        tc = float(line.rstrip('\n'))
        F.append(deCversF(tc))

with open('fahrenheit.txt', 'w') as ecriture:
    for far in F:
        print(far, file=ecriture)