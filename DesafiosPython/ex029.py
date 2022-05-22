vel = int(input('Informe a velocidade do automóvel: '));

if vel > 80:
    multa = (vel - 80) * 7;
    print('Você passou do limite de velocidade. O valor da sua multa será de: R${},00'.format(multa));
print('Dirija com segurança! Tenha um bom dia.');
print('FIM');
