import math

n1 = float(input('Insita um número real: '));
print('O valor digitado é {} e a sua porção inteira é {}'.format(n1, math.floor(n1)));

##método 2:
n2 = float(input('Insira um número real: '));
print('O valor digitado é {} e a sua porção inteira é {}'.format(n2, math.trunc(n2)));

##método 3:
n3 = float(input('Insira um número real: '));
print('O valor digitado é {} e a sua porção inteira é {}'.format(n3, int(n3)));
