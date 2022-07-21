from random import randint
from time import sleep

numeros = list()

def sortear(numeros):
    for cont in range(0,5):
        num=randint(0,10)
        numeros.append(num)
    print(f'Sorteando 5 valores da lista: {numeros}.')
    print('FEITO...', flush=True)
    sleep(0.5)

def somar(numeros):
    soma = 0

    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


sortear(numeros)
somar(numeros)