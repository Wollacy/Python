from time import sleep

def maior(*valores):
    cont = maior = 0
    print('\nAnalisando valores informados...')
    print('=+'*20)

    for valor in valores:
        print(f'{valor} ', end='', flush=True)
        sleep(0.4)

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print('-'*25)
    if len(valores) <= 1:
        print(f'Foi passado {len(valores)} valor e o maior foi {maior}.')    
    else:
        print(f'Foram passados {len(valores)} valores e o maior foi {maior}.')
    print('=+'*20)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()