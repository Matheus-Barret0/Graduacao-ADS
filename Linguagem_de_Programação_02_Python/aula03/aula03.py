from numpy.ma import append

nome = []
nota = []
media = 0

qtdAlunos = int(input('Numero de alunos:' ))
for i in range (qtdAlunos):
    nome.append(input('Digite o nome do Aluno: '))
    nota.append(float(input('Digite a nota do Aluno: ')))
    media = media + nota[i]

media = media / qtdAlunos

for i in range (qtdAlunos):
    if nota[i] > media:
        print('Parabens', nome[i])

