import datetime

cadastro = dict()

dataAtual = datetime.datetime.now() 
anoAtual = dataAtual.year

while True:
    cadastro['nome'] = str(input('Nome: '))
    anoNascimento = int(input('Ano do Nascimento: '))
    
    idade = anoAtual - anoNascimento

    cadastro['idade'] = idade
    cadastro['ctps'] = int(input('Número da carteira de Trabalho: '))

    if cadastro['ctps'] != 0:
        cadastro['anoContratacao'] = int(input('Qual o ano da contratação: '))
        cadastro['salario'] = float(input('Salário: R$ '))

    resposta = str(input('Quer continuar? S/N')).strip().upper()[0]

    if resposta == 'N':
        break

for k, v in cadastro.items():
    print(f' - {k} em {v}')