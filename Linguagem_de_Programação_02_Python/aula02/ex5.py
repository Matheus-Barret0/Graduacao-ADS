from random import randint
# somando os numeros ate achar o numero escrito
num = 5
soma = 0
x = randint(0, 10)
while num != x:
    soma = x + soma
    x = randint(0, 10)
print(soma)