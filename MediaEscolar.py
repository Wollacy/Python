## Média Escolar

n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=(n1+n2)/2

print('')

if media<5:
  print('Sua média é: {:.1f}'.format(media))
  print('\033[1;30;41mREPROVADO')
elif 7>media>=5:
  print('Sua média é: {:.1f}'.format(media))
  print('\033[1;30;43mRECUPERAÇÃO')
else:
  print('Sua média é: {:.1f}'.format(media))
  print('\033[1;30;42mAPROVADO')