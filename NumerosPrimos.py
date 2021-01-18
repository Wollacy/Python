## Números Primos

n=int(input('Digite um número: '))
e=0

for i in range(1,n+1):
  if n %i == 0:
    e += 1
    print('\033[34m', end=' ')
  else:
    print('\033[33m', end=' ')
  print('{}'.format(i), end=' ')

print('\033[0;30m')

if e != 2:
  print('O número \033[1;31m{} \033[0;30mé divisível \033[1;31m{} \033[0;30mvezes, portanto \033[1;31mNÃO É PRIMO!'.format(n,e))
else:
  print('O número \033[1;31m{} \033[0;30mé divisível \033[1;31m{} \033[0;30mvezes, portanto \033[1;32mÉ PRIMO!'.format(n,e))