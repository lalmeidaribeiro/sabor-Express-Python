#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except
#  para lidar com a divisão por zero, caso a lista esteja vazia.

lista = [2,4,5,6]
soma = 0
contador = 0 
media = 0 
for i in lista:
    contador += 1
    soma +=i 
media = (soma/contador)
print(f'O resultado da média entre {soma}/{contador} = {media}')


    