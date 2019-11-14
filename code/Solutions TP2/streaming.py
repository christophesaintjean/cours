MAX_OUT = 10**8
MAX_Q = 8000
MIN_Q = 4000

MAX_Q_ABOS = MAX_OUT / MAX_Q
MIN_Q_ABOS = MAX_OUT / MIN_Q

abos = int(input("Nombre d'abonnés ? "))

if abos <= MAX_Q_ABOS:
    print("Scénario 1")
    print('Il est possible de recruter', int(MAX_Q_ABOS - abos),
          'nouveaux abonnés à la qualité max')
    
elif abos <= MIN_Q_ABOS:
    print("Scénario 2")
    print('Taux moyen de transfert : ', round(MAX_OUT / abos, 3))
    
else:
    print("Scénario 3")
    print('Il y a', abos - MIN_Q_ABOS, 'abonnés en trop...')


