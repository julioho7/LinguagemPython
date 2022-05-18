km = float(input('Informe a kilometragem rodada: '));
dias = int(input('Informe a quantidade de dias que ele foi alugado: '));
valorTotal = (0.15 * km) + (60 * dias);
print('Com {} dias e com {}Km rodados, o valor a pagar é de R${:.2f}'.format(dias, km, valorTotal));
