## Analisar Nome

nome=str(input('Digite seu nome completo: ')).strip()
nomeCompleto=nome.split()
print('Seu primeiro nome: {}'.format(nomeCompleto[0]))
print('Seu último nome: {}'.format(nomeCompleto[len(nomeCompleto)-1]))
print('Seu nome MAIÚSCULO: {}'.format(nome.upper()))
print('Seu nome minúsculo: {}'.format(nome.lower()))
nome2=nome.strip()
print('Seu nome completo tem {} letras!'.format(len(nome2)-nome2.count(' ')))
print('Seu primeiro nome tem {} letras!'.format(nome2.find(' ')))