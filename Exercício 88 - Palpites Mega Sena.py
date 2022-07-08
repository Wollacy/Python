from random import randint
from time import sleep

lista = list()
jogos = list()

print('=' *30)
print(f"{'JOGO DA MEGA SENA':^30}")
print('=' *30)

qtdJogo = int(input('Quantos jogos você quer sortear? '))

tot = 1
while tot <= qtdJogo:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print()
print('-='*3, f' SORTEANDO {qtdJogo} JOGOS ', '-='*3)
print()

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print()
print('-='*5, ' BOA SORTE ', '-='*5)