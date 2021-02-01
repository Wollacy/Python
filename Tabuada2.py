## Tabuada com While e Break

while True:
    print('-='*30)
    print('\033[1;31mDigite um número NEGATIVO para sair!\033[m')
    print('-='*30)
    n=int(input('Digite um número para ver a sua tabuada: '))
    print('-='*30)
    if n < 0:
        break
    for i in range(0,11):
        r=n*i
        print(f'{n} X {i:2} = {r:3}')
        print('_'*30)
print('FIM!!!')