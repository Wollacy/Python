## Análise de Dados em Grupo

maiores = homens = mulheres = 0

print('CADASTRO DE PESSOAS')

while True:
    print('='*30)
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip().upper()[0]

    while sexo != 'M' and sexo != 'F':
        sexo=str(input('Escolha inválida! Sexo [M/F]: ')).strip().upper()[0]

    if idade>=18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres += 1
    
    continuar=str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    while continuar != 'S' and continuar != 'N':
        continuar=str(input('Resposta inválida! Quer continuar [S/N]? ')).strip().upper()[0]
    
    if continuar == 'N':
        break

print(f'Foram cadastrado {maiores} pessoas com mais de 18 anos. {homens} homens e {mulheres} mulheres com menos de 20 anos!')