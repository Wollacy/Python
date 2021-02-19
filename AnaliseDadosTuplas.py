## Análise de Dados em Tuplas

n= (int(input('Digite o primeiro valor: ')),
    int(input('Digite o segundo valor: ')),
    int(input('Digite o terceiro valor: ')),
    int(input('Digite o quarto valor: ')))

print(f'Você digitou os valores {n}.')

cont = par = 0

for c in n:
    if c == 9:
        cont=cont+1
    if c % 2 == 0:
        par += 1

print(f'O número 9 apareceu {cont}x!')
if 3 in n:
    print(f'O número 3 aparece pela primeira na na {n.index(3)+1}ª posição!')
else:
    print('O número 3 não foi digitado!')
print(f'Foram digitados {par} números pares!')