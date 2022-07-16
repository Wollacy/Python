from ast import Break


jogador = dict()
partidas = list()
cadastro = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

    partidas.clear()

    cont = 0
    for c in range(0, tot):
        cont += 1
        partidas.append(int(input(f'   Quantos gols na partida {cont}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    cadastro.append(jogador.copy())

    while True:
        resposta = str(input('Deseja continuar? S/N ')).strip().upper()[0]

        if resposta in 'SN':
            break

        print('Resposta inválida. Digite "S" para "SIM" ou "N" para "NÃO"!')
    
    if resposta == 'N':
            break

print('-='*10, ' JOGADORES CADASTRADOS ', '-='*10)
print(f"{'Cód.':<5}", end='')
print(f"{'Nome':<20}", end='')
print(f"{'Gols':<20}", end='')
print(f"{'Total':<10}")
print('-=' *40)
print()

cont = 0
for k, v in enumerate(cadastro):
    cont += 1
    print(f'{cont:<5}', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()

while True:
    print()
    mostrar=int(input('Qual jogador você quer detalhar? (999 para sair)'))
    print()
    
    if mostrar == 999:
        break
    
    busca=mostrar-1
    if busca >= len(cadastro):
        print(f'ERRO! Não existe jogador com o código {mostrar}')
    else:
        print(f'Levantamento do jogador {cadastro[busca]["nome"]}:')
        for i, g in enumerate(cadastro[busca]['gols']):
            print(f'      No jogo {i+1} fez {g} gols.')
        print('-'*30)

print('>>>>>>>> ATÉ MAIS! <<<<<<<<')