#Definindo funções e métodos para o objeto a.

a = input('Digite algo que esteja em sua mente: ');
print('O tipo primitivo do valor informado é: ', type(a)); #Verificar qual o tipo primitivo
print('Só tem espaços? ', a.isspace()); #Verificar se tem somente espaços
print('É um número? ', a.isnumeric()); #Verificar se é somente um número
print('É um alfabeto? ', a.isalpha()); #Verificar se é somente do alfabeto
print('É um Alfanumérico? ', a.isalnum()); #Verificar se é alfanumérico
print('Está em MAIÚSCULAS? ', a.isupper()); #Verificar se está em Maíuscula somente
print('Está em minúsculas? ', a.islower()); #Verificar se está em minúsculas somente
print('Está capitalizada? ', a.istitle()); ##Verificar se está somente a primeira letra é maiúscula

#Essas difinições podem ser utilizadas para senhas
