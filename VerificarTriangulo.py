## Verifica Triângulo - Exercício 35

ladoA=float(input('Digite o primeiro lado: '))
ladoB=float(input('Digite o segundo lado: '))
ladoC=float(input('Digite o terceiro lado: '))

if ladoA<(ladoB+ladoC) and ladoB<(ladoC+ladoA) and ladoC<(ladoA+ladoB):
  print('É possível formar um triângulo!')
else:
  print('Não é possível formar um triângulo!')