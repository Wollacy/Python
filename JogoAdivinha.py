## Jogo de adivinhação

import random
from time import sleep
pc=random.randint(0, 5)

print('Vou pensar em um número entre 0 e 5 tente adivinhar!')
n=int(input('Digite um número: '))

print('Processando...')
sleep(2)

if n==pc:
  print('Acerto Miserávi, pensei no número {}'.format(pc))
else:
  print('Errrrrrrrrooouuuu, pensei no número {} e não o número {}!'.format(pc, n))