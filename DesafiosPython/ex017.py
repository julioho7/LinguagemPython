## from math import hypot
import math
co = float(input('Informe o valor do Cateto Oposto: '));
ca = float(input('Informe o valor do Cateto Adjacente: '));
hi = (co ** 2 + ca ** 2) ** (1/2);
print('O valor da hipotenuza é {:.2f}'.format(hi));

##método 2:
co = float(input('Informe o valor do Cateto Oposto: '));
ca = float(input('Informe o valor do Cateto Adjacente: '));
hi = math.hypot(co, ca);
print('O valor da hipotenuza é {:.2f}'.format(hi));