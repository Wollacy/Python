import datetime

cadGeral = list()
cadastro = dict()

dataAtual = datetime.datetime.now() 
anoAtual = dataAtual.year

while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: '))
    anoNascimento = int(input('Ano do Nascimento: '))
    
    idade = anoAtual - anoNascimento

    cadastro['idade'] = idade
    cadastro['ctps'] = int(input('Número da carteira de Trabalho: '))

    if cadastro['ctps'] != 0:
        cadastro['anoContratacao'] = int(input('Qual o ano da contratação: '))
        cadastro['salario'] = float(input('Salário: R$ '))
        cadastro['aposentadoria'] = cadastro['idade'] + (cadastro['anoContratacao'] + 35) - anoAtual

    cadGeral.append(cadastro.copy())

    while True:
        resposta = str(input('Quer continuar? S/N ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Resposta inválida. Selecione apesa "S" ou "N"!')

    if resposta == 'N':
        break

print('*='*30)
for p in cadGeral:
    for k, v in p.items():
        print(f'{k} = {v}; ', end='')
    print()

print('*='*30)
for p in cadGeral:
    if p['ctps'] > 0:
        print(f'{p["nome"]} vai se aposentar com {p["aposentadoria"]} anos.')

print('*='*30)
print('>>>>>>>>>> FINALIZADO <<<<<<<<<<')