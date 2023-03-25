turma = []
for i in range(3):
    #criar linha vazia
    linha = []
    for j in range(5):
        #vai adicionar as notas na linha
        linha.append(int(input('Digite a nota [' + str(i) + ',' + str(j) + ']:' )))

    #adiciona a linha na matriz turma
    turma.append(linha)

for i in range(3):
    print(turma)