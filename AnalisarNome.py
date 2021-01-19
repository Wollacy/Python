## Analisar Nome

nome=str(input('Digite seu nome completo: ')).strip()
nomeCompleto=nome.split()
print('Seu primeiro nome: {}'.format(nomeCompleto[0]))
print('Seu último nome: {}'.format(nomeCompleto[len(nomeCompleto)-1]))