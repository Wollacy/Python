def lin():
    print('-'*30)

def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

def soma(a, b):
    s = a + b
    print(f'O resultado entre {a} + {b} é {s}')
    lin()

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores de {num} e são ao todo {tam} números!')
    lin()
    for valor in num:
        print(f'{valor} ', end='')
    print()
    lin()

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


lin()
print('Curso de Python')
lin()
lin()
print('Wollacy')
lin()

mensagem('SISTEMAS DE ALUNOS')

soma(4, 5)
soma(8, 9)
soma(2, 1)

contador(1, 2, 3)
contador(4, 5)
contador(6, 7, 8, 9, 0)

valores = [1, 2, 3, 4, 5]
lin()
print(valores)
lin()
dobra(valores)
lin()
print(valores)
lin()