import math
an = float(input('Informe um angulo qualquer: '));
seno = math.sin(math.radians(an));
print('O angulo de {} tem o SENO de {:.2f}'.format(an, seno));
cos = math.cos(math.radians(an));
print('O angulo de {} tem COSENO de {:.2f}'.format(an, cos));
tan = math.tan(math.radians(an));
print('O angulo de {} possui Tangente de {:.2f}'.format(an, tan));
