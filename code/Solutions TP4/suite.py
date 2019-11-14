u0 = float(input("u0 ? "))
r = float(input("r  ? "))

n = None

while n is None or n < 0:
    n = int(input("n  ? "))

print('Les', n, 'premiers termes sont:')
n_ = 0
un_ = u0
while n_ < n:
    print(un_, end=' ')
    n_ = n_ + 1
    un_ = un_ + r
