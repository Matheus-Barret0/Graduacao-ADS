#testando Matriz

turma = [[5.0,2.0,4.0,1.0,8.0],[8.0,1.0,4.0,2.0,5.0], [6.0,4.0,8.0,5.0,9.0]]

#calcular media
media = 0
#for para percorrer as linhas
for i in range(3):
    #for para percorrer as colunas
    for j in range(5):
        media = media + turma[i][j]
media = media / 15
print(media)