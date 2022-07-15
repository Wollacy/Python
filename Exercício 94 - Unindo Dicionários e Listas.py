pessoas = list()
cadastro = dict()

soma = media = 0

while True:
    cadastro.clear()
    
    cadastro['nome'] = str(input('Nome: '))
    
    while True:
        cadastro['sexo'] = str(input('Sexo: M/F ')).strip().upper()[0]

        if cadastro['sexo'] == 'M' or cadastro['sexo'] == 'F':
            break
        print('Resposta inválida. Sexo deve ser "M" ou "F"!')
    
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']

    pessoas.append(cadastro.copy())

    while True:
        resp = str(input('Deseja continuar? S/N ')).strip().upper()[0]

        if resp in 'SN':
            break
        
        print('Resposta inválida. Resposta deve ser "S" ou "N"!')

    if resp == 'N':
        break

print('*='*30)
print(f'Ao todo foram cadastrados {len(pessoas)} pessoas.')

media = soma / len(pessoas)

print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        print(f'   ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('>>>>>>>>>> ENCERRADO <<<<<<<<<<')