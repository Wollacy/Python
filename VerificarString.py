## Verificar uma String

nome=str(input('Qual seu nome? '))
print('')

if nome == 'Wollacy':
  print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
  print('Nome popular no Brasil!')
else:
  print('Nome comum!')
print('')
print('Olá {}!'.format(nome))