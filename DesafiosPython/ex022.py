nome = str(input('Informe o seu nome e vamos ele se transformar: ')).strip();
print(nome.upper());
print(nome.lower());
print('O seu nome possui {} letras.'.format(len(nome) - nome.count(' ')));
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')));
separa = nome.split();
print('Seu primeiro nome é {} e ele possui {} letras.'.format(separa[0], len(separa[0])));
