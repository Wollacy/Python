listaPrincipal = [[], []]
numero = 0

for cont in range(1,8):
    numero = int(input(f'Digite o {cont}º valor: '))
    if numero % 2 == 0:
        listaPrincipal[0].append(numero)
    else:
        listaPrincipal[1].append(numero)

listaPrincipal[0].sort()
listaPrincipal[1].sort()

print('-=' * 30)
print(f'Os valores pares digitados foram: {listaPrincipal[0]}')
print('-=' * 30)
print(f'Os valores ímpares digitados foram: {listaPrincipal[1]}')
print('-=' * 30)