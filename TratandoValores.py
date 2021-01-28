## Tratando Vários Valores

n = t = c = 0

while n != 999:
    n=int(input('Digite um número [999 para sair]: '))
    if n != 999:
        t += n
        c += 1
    else:
        print('-='*20)
        print('Fim...')
print('-='*20)
print('Você digitou {} números e a soma entre eles foi {}.'.format(c, t))
print('-='*20)