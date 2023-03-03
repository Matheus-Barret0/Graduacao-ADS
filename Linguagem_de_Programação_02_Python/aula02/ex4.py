#fatorial de um numero
numero = int(input("Fatorial de: "))
resultado = 1
numTotal = 1
while numTotal <= numero:
    resultado *= numTotal
    numTotal += 1
print(resultado)