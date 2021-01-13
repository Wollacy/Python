## Gerenciando Pagamentos

print('{:=^40}'.format(' Loja do Wollacy '))
valor=float(input('Qual valor da compra? '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro
[2] débito
[3] até 3x cartão
[4] mais de 3x no cartão
''')
opcao=int(input('Escolha a opção de pagamento: '))

if opcao==1:
  valorFinal=valor-(valor*10/100)
  print('Valor total= R$ {:.2f}'.format(valorFinal))
elif opcao==2:
  valorFinal=valor-(valor*5/100)
  print('Valor total= R$ {:.2f}'.format(valorFinal))
elif opcao==3:
  valorFinal=valor
  parcela=int(input('Digite o número de parcelas: '))
  vlrParcela=valorFinal/parcela
  print('Sua compra parcelada em {}x SEM juros. Valor de R$ {:.2f} por parcela. Valor total= R$ {:.2f}'.format(parcela, vlrParcela, valorFinal))
elif opcao==4:
  valorFinal=valor+(valor*20/100)
  parcela=int(input('Digite o número de parcelas: '))
  vlrParcela=valorFinal/parcela
  print('Sua compra parcelada em {}x COM juros de 20%. Valor de R$ {:.2f} por parcela. Valor total= R$ {:.2f}'.format(parcela, vlrParcela, valorFinal))
else:
  print('Opção inválida!')