import random
from time import sleep

n1 = random.randint(1, 5);
n2 = int(input('Entre 1 e 5, em que número eu estou pensando? '));

if n1 == n2:
    print('Processando..');
    sleep(2)
    print('Você me venceu! Parabéns.');
else:
    print('Processando..');
    sleep(2)
    print('Você errou, o número que você falou foi {} e o número que eu pensei foi {}.'.format(n2, n1));
