## Tabuada

n=int(input('Escolha um número para mostrar a tabuada: '))

for i in range(0,11):
  r=n*i
  print('{} X {:2} = {:3}'.format(n,i,r))