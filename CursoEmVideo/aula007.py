##Operadores aritméticos
## ** potência
## % resto da divisão - Esse será o resto da divisão
## // divisão inteira - Esse será o quociente da divisão

print(int(5+2));
print(int(5-2));
print(int(5*2));
print(int(5/2));
print(int(5**2));
print(int(5//2));
print(int(5%2));
pow(5, 2);
oi = 'oi' * 5;
print(oi);

nome = input('Qual é o seu nome? ');
print('Prazer em te conhecer {:>20}!'.format(nome)); ## Espaço a esquerda
print('Prazer em te conhecer {:<20}!'.format(nome)); ## Espaço a direita
print('Prazer em te conhecer {:^20}!'.format(nome)); ## centralizado nos espaços
print('Prazer em te conhecer {:=^20}!'.format(nome)); ## centralizado nos espaços preenchendo com =

n1 = int(input('Indique o primeiro número: '));
n2 = int(input('Indique outro número: '));
s = n1 + n2;
m = n1 * n2;
d = n1 / n2;
di = n1 // n2;
e = n1 ** n2;
print('A soma é {}, \no produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ');
print('Divisão inteira é {} e potência {}'.format(di, e));

## Ordem de precedência:
## 1 - ()
## 2 - **
## 3 - * - / - // - %
## 4 - + -