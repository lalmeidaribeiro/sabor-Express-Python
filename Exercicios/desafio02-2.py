#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura 
# if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

i = int(input('Informe sua idade: '))

if i <= 12:
    print('Criança')
elif i >= 13 and i <= 18:
    print('Adolescente')
else:
    print('Adulto')