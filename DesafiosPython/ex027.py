n = str(input('Insira seu nome completo: '));
nome = n.split();
print('Muito prazer em te conhecer {}!'.format(n));
print('O seu primeiro nome é {}.'.format(nome[0]));
print('O seu úlimo nome é {}.'.format(nome[len(nome) - 1]));
