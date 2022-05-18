import math
import random

n = int(input('Informe um valor: '));
raiz = math.sqrt(n);
print('A raiz quadrada de {} é {}'.format(n, raiz));

n1 = random.random() ##Irá gerar um número aleatório entre 0 e 1
print('\nO número gerado aleatóriamente foi: ', n1);
n2 = random.randint(1, 10); ##Irá gerar um número inteiro entre os dois números selecionados
print('\nO número gerado aleatóriamente nesse caso foi: ', n2);
