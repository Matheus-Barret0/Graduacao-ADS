num1 = int(input('Digite o primeiro numero: \n'))
num2 = int(input('Digite o segundo numero: \n'))
num3 = int(input('Digite o terceiro numero: \n'))

# Ordenar em ordem crescente
if num1 < num2 and num2 < num3:
    print(num1, num2, num3)
elif num2 < num3 and num3 < num1:
    print(num2, num3, num1)
elif num3 < num1 and num1 < num2:
    print(num3, num1, num2)
else:
    print(num3, num2, num1)

# Ordenar em ordem decrescente
if num1 > num2 and num2 > num3:
    print(num1, num2, num3)
elif num2 > num3 and num3 > num1:
    print(num2, num3, num1)
elif num3 > num1 and num1 > num2:
    print(num3, num1, num2)
else:
    print(num3, num2, num1)
