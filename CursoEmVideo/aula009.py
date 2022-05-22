##Fatiamento de String

frase = 'Curso em Vídeo Python';
print('Nesse caso irá mostrar o nono espaço ou décima letra: {}'.format(frase[9]));
print('Nesse caso irá mostrar do nono espaço até o 13 espaço: {}'.format(frase[9:14]));
print('Nesse caso irá mostrar do nono espaço até o 20 espaço pulando de 2 em 2: {}'.format(frase[9:21:2]));
print('Nesse caso, irá mostrar do começo da frase, até a posição 4: {}'.format(frase[:5]));
print('Nesse caso irá mostrar da posição 15 até o final: {}'.format(frase[15:]));
print('Nesse caso irá mostrar da posição 9 até o final, pulande de 3 em 3: {}'.format(frase[9::3]));

##Análise da String
print('\nTamanho da frase: {}'.format(len(frase)));
print('\nQuantas vezes aparece a letra o: {}'.format(frase.count('o'))); ##Contar quantas vezes aparece a letra o, neste caso.
print('\nQuantas vezes aparece a letra o da posição 0 até as 12: {}'.format(frase.count('o', 0, 13)));
print('\nEm qual posição começa a frase descrita: {}'.format(frase.find('deo')));
print('\nSe não tiver ANDROID, fica -1'.format(frase.find('Android')));
print('\nMostra se possui a palavra descrita na variável criada: {}'.format('Curso' in frase));

##Tranformação
print('Nesse caso, substituiu uma palavra por outra'.format(frase.replace('Python', 'Android')));
print('Colocar toda a frase em letra maiúscula: {}'.format(frase.upper()));
print('Colocar toda a frase em letra minúscula: {}'.format(frase.lower()));
print('Coloca somente a primeira letra em maiúscula: {}'.format(frase.capitalize()));  ##Somente a primeira letra da frase em Maiúscula
print('Coloca todas as primeiras letras em maiúscula: {}'.format(frase.title())); ##Todas as primeiras letras em Maiuscula
print('Remove os espaços inúteis do início e final: {}'.format(frase.strip())); ##Remove todos os espaços inúteis da frente e no final da frase.
print('Remove os espaços da direita: {}'.format(frase.rstrip())); ##Remove somente os espaços da direita
print('Remove os espaços da esquerda: {}'.format(frase.lstrip())); ##Remove somente os espaços da esquerda

##Divisão
print(frase.split());
print('-'.join(frase));