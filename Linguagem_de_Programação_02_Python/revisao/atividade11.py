#11.Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes existem no vetor.

vetor = [10]
for i in range(10):
    valor = int(input(f"Digite o valor da posição {i}: "))
    vetor.append(valor)

diferentes = set(vetor)
quantidade = len(diferentes)

print(f"No vetor digitado existem {quantidade} valores diferentes.")