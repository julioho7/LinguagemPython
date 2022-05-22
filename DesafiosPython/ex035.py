print('Analisando a formação de um triangulo')
l1 = float(input('Informe o valor do primeiro lado: '))
l2 = float(input('Informe o valor do segundo lado: '))
l3 = float(input('Informe o valor do terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo com esses valores')

print('FIM')