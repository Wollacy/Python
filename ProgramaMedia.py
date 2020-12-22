##Estruturas Condicionais - Média

n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m=(n1+n2)/2

if m >= 7:
  print('Você está acima na média {:.1f}'.format(m))
else:
  print('Você está abaixo da média {:.1f}'.format(m))