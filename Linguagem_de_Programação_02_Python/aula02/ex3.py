#imprima a quantidade de numero de pares escolhidos pelo usuario
numRecebe1 = int(input('Inicio'))
numRecebe2 = int(input('Final'))
numTotal = 0
while numRecebe1 <= numRecebe2:
    if numRecebe1 % 2 == 0:
        numTotal = numTotal + 1
print(numTotal)