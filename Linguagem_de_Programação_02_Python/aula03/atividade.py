from random import randint
vet = []
contador = 0

for i in range(50):
    vet.append(randint(0, 10))
    if 6 in vet:
        contador += 1

porcentagem = contador/50*100
print(porcentagem,'%')