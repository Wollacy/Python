## Maior e Menor Valor em Tupla

from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('-='*50)
print(f'Os números sorteados foram: {n}')
print('-='*50)
print(f'O menor valor foi: {min(n)}')
print('-='*50)
print(f'O maior valor foi: {max(n)}')
print('-='*50)