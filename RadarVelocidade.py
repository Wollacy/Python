## Radar eletrônico

v=int(input('Qual a velocidade do carro? '))
if v>80:
  multa=(v-80)*7
  print('Você foi multado! O valor da multa é de {:.2f}'.format(multa))
else:
  print('Boa Viagem!')