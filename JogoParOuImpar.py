## Jogo de Par ou Impar com o Computador

import random
from time import sleep
pc=random.randint(0, 10)

print('='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')

sair = cont = 0

while True:
    pc=random.randint(0, 10)
    
    print('='*30)
    n=int(input('Digite um valor: '))
    e=str(input('[P] Par ou [I] Ímpar? ')).upper()
    
    while e != 'P' and e != 'I':
        e=str(input('Escolha inválida! Escolha [P] para Par ou [I] para Ímpar?')).upper()
    
    tot=pc+n
    
    if tot %2 == 0:
        if e == 'P':
            print(f'O computador colocou {pc} e você colocou {n}!')
            print(f'Você venceu! {tot} é par.')
        else:
            print(f'O computador colocou {pc} e você colocou {n}!')
            print(f'Você perdeu! {tot} é par.')
            sair = 1
    else:
        if e == 'I':
            print(f'O computador colocou {pc} e você colocou {n}!')
            print(f'Você venceu! {tot} é ímpar.')
        else:
            print(f'O computador colocou {pc} e você colocou {n}!')
            print(f'Você perdeu! {tot} é ímpar.')
            sair = 1
    if sair == 1:
        print('Fim de Jogo.')
        break
    cont += 1

print('='*30)
print(f'Houve {cont} vitórias consecutivas.')