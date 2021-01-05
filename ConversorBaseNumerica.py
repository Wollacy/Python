## Conversor de Bases Numéricas

n1=int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
escolha=int(input('''
[1] Para Binário
[2] Para Octal
[3] Para Hexadecimal
'''))
if escolha==1:
  print('{} em Base binária é: {}'.format(n1, bin(n1)[2:]))
elif escolha==2:
  print('{} em Base octal é: {}'.format(n1, oct(n1)[2:]))
elif escolha==3:
  print('{} em Base hexadecimal é: {}'.format(n1, hex(n1)[2:]))
else:
  print('Escolha inexistente: {}'.format(escolha))