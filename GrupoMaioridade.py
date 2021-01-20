## Grupo da Maioridade
from datetime import date

atual=date.today().year
maior=0
menor=0

for n in range(1,8):
  ano=int(input('Digite o ano de nascimento da {}ª pessoa: '.format(n)))
  idade = atual - ano

  if idade > 21:
    maior += 1
  else:
    menor += 1

print('='*40)
print('Neste grupo existe {} pessoas maiores de idade e {} pessoas menores de idade.'.format(maior, menor))