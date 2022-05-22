km = int(input('Informe a kilometragem da viagem: '));

if km > 200:
    prec = float(0.45) * km;
    print('O valor da sua passagem será de R${:.2f}'.format(prec))
else:
    prec = float(0.50) * km;
    print('O valor da sua passagem será de R${:.2f}'.format(prec))