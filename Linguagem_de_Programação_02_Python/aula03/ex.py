numero = [1,4,3,2,5]
numero2 = [1,2,5,9,10]

for i in range(5):
    if numero[i] and numero2[i] == 10:
        print(f'Lista contem numero 10, na posicao {i}')
    else:
        print('Lista sem o numero 10')