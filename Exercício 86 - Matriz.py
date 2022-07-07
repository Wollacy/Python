## matriz = [[0, 0], [0, 0], [0, 0]]
matriz = [[], [], []]

for lin in range(0,3):
    for col in range(0,3):
        numero = int(input(f'Digite um valor para [{lin}, {col}]: '))
        matriz[lin].append(numero)

        ## matriz[lin][col]=int(input(f'Digite um valor para [{lin}, {col}]: '))

print('-=' * 25)
for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
print('-=' * 25)