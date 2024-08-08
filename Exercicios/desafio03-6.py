#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.

lista = [2,5,6]
soma = 0
i=0
try:
  for i in lista:
       soma +=i
  print(f'A soma dos número {lista} é {soma}')
except Exception as e:
   print(f"Ocorreu um erro: {e}")