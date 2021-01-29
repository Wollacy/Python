## Maior Menor e Media com While

resposta='S'
c = tot = 0

while resposta == 'S':
    n=int(input('Digite um número: '))
    if c == 0:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    c += 1
    tot += n
   
    resposta=str(input('Deseja continuar? [S/N]')).upper()

m = tot / c

print('-='*15)
print('Você digitou {} números, a soma entre eles é de {} e a média é de {:.2f}.'.format(c, tot, m))
print('-='*15)
print('O MENOR número digitado foi {}, e o MAIOR foi {}.'.format(menor, maior))
print('-='*15)
print('FIM!')