#Lista de exercícios Pyhton 02

#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

n = int(input('Informe um número: '))
if n % 2 == 0:
    print(f'{n} é par!!')
else:
    print(f'{n} é impar!')