## Aumentos Múltiplos

salario=float(input('Digite o salário do funcionário: '))

if salario <= 1250:
  porcento=15
  novoSalario=salario+(salario*15/100)
else:
  porcento=10
  novoSalario=salario+(salario*10/100)

print('Para o salário {:.2f} o aumento será de {:.2f}%. O novo salário é {:.2f}'.format(salario, porcento, novoSalario))