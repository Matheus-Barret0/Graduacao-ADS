#10.Faça um programa que receba dois números inteiros e gere os números pares que estão no intervalo compreendido por eles.

num1 =int(input('Digite o primeiro numero: '))
num2 =int(input('Digite o segundo numero: '))

for i in range(num1, num2, 1):
        print(i)
