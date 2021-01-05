## Aprovando Empréstimos

valor=float(input('Valor da casa: R$ '))
salario=float(input('Salário do comprador: R$ '))
ano=int(input('Quanto anos de financiamento? '))

prestacao=valor/(ano*12)
porcento=salario*0.30

print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}!'.format(valor, ano, prestacao))

if porcento<=prestacao:
  print('Empréstimo NEGADO!!!')
else:
  print('Empréstimo CONCEDIDO!!!')