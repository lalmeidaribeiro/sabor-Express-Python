#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = input('Informe uma frase ou palavra: ')

contagem_palavras = {}
palavras = frase.split( )

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    
print(contagem_palavras)