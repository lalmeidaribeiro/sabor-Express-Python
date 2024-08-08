#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
n = int(input('Digite um número: '))
i = 0 
print(f'A tabuada do número {n} é:\n')
for i in range(1,11):
    t = i*n
    print(f'{i} x {n} = {t}')

