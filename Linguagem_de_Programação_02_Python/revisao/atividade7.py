#7.Faça um programa que leia 5 números e informe o maior número.

primeiro = int(input('Primeiro numero: '))
segundo = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))
quarto = int(input('Quarto numero : '))
quinto = int(input('Quinto numero: '))

menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro
if (quarto < menor):
    menor = quarto
if (quinto < menor):
    menor = quinto

print('Menor: ', menor)