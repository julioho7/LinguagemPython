sal = float(input('Informe o seu salário: '));

if sal > 1250:
    sal = ((sal * 10) / 100) + sal
else:
    sal = ((sal * 15) / 100) + sal
print('O seu salário com aumento será de R${:.2f}'.format(sal))