#12.Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) está no vetor.
# Caso o valor x não seja encontrado, o programa deve imprimir o valor -1.

posicao = -1
vetor = [5]
for i in range(5):
    valor = int(input(f"Digite o valor da posição {i}: "))
    vetor.append(valor)

numeroProcurando = int(input("Digite o valor a ser buscado: "))

for i in range(len(vetor)):
    if vetor[i] == numeroProcurando:
        posicao = i

if posicao == -1:
    print(numeroProcurando)
else:
    print(f"{numeroProcurando} na posição {posicao}.")

