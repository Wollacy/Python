## Cálculo IMC

peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))

imc=peso/(altura*altura)

print('Seu IMC é de: {:.2f}'.format(imc))

if imc<18.5:
  print('ABAIXO DO PESO')
elif imc>=18.5 and imc<25:
  print('PESO NORMAL')
elif imc>=25 and imc<30:
  print('ACIMA DO PESO')
elif imc>=30 and imc<35:
  print('OBESSIDADE GRAU 1')
elif imc>=35 and imc<40:
  print('OBESSIDADE GRAU 2')
else:
  print('OBESSIDADE MÓRBIDA')