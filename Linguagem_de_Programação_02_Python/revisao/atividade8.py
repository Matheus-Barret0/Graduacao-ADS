#8.Faça um programa que leia 5 números e informe a soma e a média dos números.

num1 = int(input('Digite o primeiro numero para ser somado: '))
num2 = int(input('Digite o segundo numero para ser somado: '))
num3 = int(input('Digite o terceiro numero para ser somado: '))
num4 = int(input('Digite o quarto numero para ser somado: '))
num5 = int(input('Digite o segundo numero para ser somado: '))

soma = (num1 + num2 + num3 + num4 + num5)
media = soma/5

print('Soma', soma)
print('Media', media)