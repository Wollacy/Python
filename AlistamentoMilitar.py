## Alistamento Militar

ano=int(input('Digite o ano do seu nascimento: '))
idade=2020-ano

if idade<18:
  alistar=ano+18
  falta=alistar-2020

  print('Para quem nasceu em {}, deve se alistar em {}!'.format(ano, alistar))
  print('Falta {} anos para o seu alistamento!'.format(falta))
elif idade>18:
  passou=ano+18
  print('Quem tem {} anos, deveria ter se alistado em {}!'.format(idade, passou))
else:
  print('Você nasceu em {}, com {} anos, deve se alistar IMEDIATAMENTE!'.format(ano, idade))