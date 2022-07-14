jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

cont = 0
for c in range(0, tot):
    cont += 1
    partidas.append(int(input(f'   Quantos gols na partida {cont}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}!')

print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i+1}, fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols')