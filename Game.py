##Game Pedra, Papel, Tesoura

from random import randint
from time import sleep

itens=['Pedra','Papel','Tesoura']
##computador=randint(0,2)
computador=2
print('='*25)
print('GAME PAPEL, PEDRA, TESOURA')
print('='*25)

usuario=int(input('''Sua escolha:
0-Pedra
1-Papel
2-Tesoura
'''))

print('JÓ')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('*'*20)

if computador==0:       ##Computador escolheu Pedra
  if usuario==1:        ##Usuário escolheu Papel
    print('Você Venceu!!!')
  elif usuario==2:      ##Usuário escolheu Tesoura
    print('Você Perdeu!!!')
  elif usuario==0:      ##Usuário escolheu Papel
    print('Empate!!!')
  else:
    print('Escolha Inválida!!!')
elif computador==1:     ##Computador escolheu Papel
  if usuario==0:        ##Usuário escolheu Pedra
    print('Você Perdeu!!!')
  elif usuario==1:      ##Usuário escolheu Papel
    print('Empate!!!')
  elif usuario==2:      ##Usuário escolheu Tesoura
    print('Você Venceu!!!')
  else:
    print('Escolha Inválida!!!')
elif computador==2:     ##Computador escolheu Tesoura
  if usuario==0:        ##Usuário escolheu Pedra
    print('Você Venceu!!!')
  elif usuario==1:      ##Usuário escolheu Papel
    print('Você Perdeu!!!')
  elif usuario==2:      ##Usuário escolheu Tesoura
    print('Empate!!!')
  else:
    print('Escolha Inválida!!!')
print('*'*20)
if usuario<=2:
  print('O computador escolheu: {}'.format(itens[computador]))
  print('Você escolheu: {}'.format(itens[usuario]))