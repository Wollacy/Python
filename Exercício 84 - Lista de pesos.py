##Exercício 84 - Lista de pesos

cadastro = list()
dado = list()

menorPeso = maiorPeso = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    
    if len(cadastro) == 0:
        maiorPeso = menorPeso = dado[1]
    else:
        if dado[1] > maiorPeso:
            maiorPeso = dado[1]
        if dado[1] < menorPeso:
            menorPeso = dado[1]

    cadastro.append(dado[:])
    dado.clear()

    continuar=str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    while continuar != 'S' and continuar != 'N':
        continuar=str(input('Resposta inválida! Quer continuar [S/N]? ')).strip().upper()[0]
    
    if continuar == 'N':
        break
    
print(f'Ao todo, você cadastrou {len(cadastro)} pessoas!')
print(f'O maior peso foi {maiorPeso}Kg. Foi o peso de: ', end='')

for p in cadastro:
    if p[1] == maiorPeso:
        print(f' {p[0]} |', end='')

print('')
print(f'O menor peso foi {menorPeso}Kg. Foi o peso de: ', end='')

for p in cadastro:
    if p[1] == menorPeso:
        print(f' {p[0]} |', end='')