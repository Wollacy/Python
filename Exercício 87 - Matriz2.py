## matriz = [[0, 0], [0, 0], [0, 0]]
matriz = [[], [], []]
somaPar = somaCol = maior = 0

for lin in range(0,3):
    for col in range(0,3):
        numero = int(input(f'Digite um valor para [{lin}, {col}]: '))
        matriz[lin].append(numero)

        ## matriz[lin][col]=int(input(f'Digite um valor para [{lin}, {col}]: '))
        if numero % 2 == 0:
            somaPar = somaPar + numero
        if col == 2:
            somaCol = somaCol + numero
        if col == 1:
            if numero > maior:
                maior = numero

print('-=' * 25)
for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
print('-=' * 25)
print(f'A soma dos valores pares é: {somaPar}')
print('-=' * 25)
print(f'A soma dos valores da terceira coluna é: {somaCol}')
print('-=' * 25)
print(f'O maior valor da segunda coluna é: {maior}')
print('-=' * 25)