import datetime
ano = int(input('Digite o ano e verifique se é um ano bissexto. Caso queira ver o ano atual, digite 0: '));

if ano == 0:
    ano = datetime.date.today().year;

cont = ano % 4;

if cont == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano));
print('FIM');