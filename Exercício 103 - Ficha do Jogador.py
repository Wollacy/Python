def ficha(jogador='<desconhecido>', gols=0):
    print('=-'*30)
    print(f'O jogador {jogador} fez ({gols}) gols no campeonato.')
    print('=-'*30)


nome = str(input('Digite o nome do jogador: '))
qtdG = str(input('Informe quantos gols ele fez: '))

if qtdG.isnumeric():
    qtdG = int(qtdG)
else:
    qtdG = 0

if nome.strip() == '':
    ficha(gols = qtdG)
else:
    ficha(nome, qtdG)