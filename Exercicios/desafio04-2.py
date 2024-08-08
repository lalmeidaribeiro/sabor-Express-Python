#2 - Utilizando o dicionário criado no item 1:

#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.

pessoa = {'nome':'Larissa', 'idade': 20, 'cidade':'São Paulo'}

pessoa['idade'] = 21
pessoa['sobrenome'] = 'Ribeiro'
del pessoa['sobrenome']

print(pessoa)