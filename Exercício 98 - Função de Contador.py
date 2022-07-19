import antigravity
from time import sleep

def contador(i, f, s):
    if s < 0:
        s *= -1
    if s == 0:
        s = 1
    
    print('-='*20)
    print(f'Contando de {i} até {f} de {s} em {s}.')
    print('-='*20)
    
    cont = i
    if i < f :
        while cont <= f:
            print(cont, end=' ', flush=True)
            cont += s
            sleep(0.5)
    else:
        while cont >= f:
            print(cont, end=' ', flush=True)
            cont -= s
            sleep(0.5)

    print()


contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))
salto = int(input('Digite o valor do salto: '))

contador(inicio, final, salto)