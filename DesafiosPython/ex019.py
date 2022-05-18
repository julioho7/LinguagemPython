import random
al1 = input('Informe o nome do primeiro aluno: ');
al2 = input('Informe o nome do segundo aluno: ');
al3 = input('Informe o nome do terceiro aluno: ');
al4 = input('Informe o nome do quarto aluno: ');

lista = [al1, al2, al3, al4];
escolhido = random.choice(lista);

print('O aluno escolhido é: {}'.format(escolhido));
