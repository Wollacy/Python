## Custo da Viagem

distancia=float(input('Qual a quilometragem da viagem? '))

if distancia<=200:
  custo=distancia*0.50
  print('O custo da viagem para {:.2f}Km é de {:.2f}'.format(distancia, custo))
else:
  custo=distancia*0.45
  print('O custo da viagem para {:.2f}Km é de {:.2f}'.format(distancia, custo))