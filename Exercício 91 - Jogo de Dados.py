from random import randint
from time import sleep
from operator import itemgetter

jogos = {'jogador1':randint(1,6),
    'jogador2':randint(1,6),
    'jogador3':randint(1,6),
    'jogador4':randint(1,6)}

ranking = dict()

print('*='*30)
print('========= VALORES SORTEADOS =========')
print('*='*30)
print()
for k, v in jogos.items():
    print(f'O {k} tirou {v}!')
    sleep(1)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print()
print('*='*30)
print('========= RANKING =========')
print('*='*30)
print(ranking)

cont = 0
for k, v in ranking.items():
    cont += 1
    print(f'{cont}º lugar: {k} com {v}!')
    sleep(1)