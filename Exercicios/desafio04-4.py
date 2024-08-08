#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

dicionario = {'nome': 'Larissa', 'sobrenome': 'Ribeiro', 'idade': 20}

chave = input('Informe uma chave para verificar se ela está dentro do dicionário: ')

if chave in dicionario:
    print('Já existe essa chave nesse dicionário!')
else:
    print('Essa chave não está dentro do dicionário!')