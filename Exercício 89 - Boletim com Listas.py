alunos = list()
temp = list()

while True:
    temp.append(str(input('Nome do Aluno: ')))
    temp.append(float(input('Primeira Nota: ')))
    temp.append(float(input('Segunda Nota: ')))

    print()

    alunos.append(temp[:])
    temp.clear()

    resp=str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print()

    while resp != 'S' and resp != 'N':
        print('Resposta Inválida!')
        resp=str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        print()

    if resp == 'N':
        break

print('-='*3, ' ALUNOS CADASTRADOS ', '-='*3)
print(f"{'Nº':<5}", end='')
print(f"{'Nome':<20}", end='')
print(f"{'Média':^10}")
print('-=' *20)
print()

cont = 0
for p in alunos:
    media = (p[1] + p[2]) / 2
    cont += 1
    print(f'{cont:<5}', end='')
    print(f'{p[0]:<20}', end='')
    print(f'{media:^10.1f}')
    print()

print('-=' *20)

while True:
    resp=int(input('Deseja mostrar a nota de qual aluno? [Tecle "0" para sair] '))
    print()
    
    escolha = resp-1
    
    if resp > len(alunos):
        print('Valor inválido!')
    elif resp == 0:
        print('Finalizando....')
        break
    else:
        print(f'Aluno: {alunos[escolha][0]}. Notas: {alunos[escolha][1]}  {alunos[escolha][2]}')
    print()

print('Até mais...')