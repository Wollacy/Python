## Estatísticas em Produtos

print('BEM VINDO! ESCOLHA SEU PRODUTO.')

total = caro = cont = 0

while True:
    print('-'*30)
    prod=str(input('Nome do Produto: '))
    preco=float(input('Preço: R$ '))
    
    if cont == 0:
        nomeMaisBarato=prod
        maisBarato=preco

    total += preco

    if preco >= 1000:
        caro += 1

    if preco < maisBarato:
        nomeMaisBarato=prod
        maisBarato=preco

    sair=str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

    while sair != 'S' and sair != 'N':
        print('RESPOSTA INVÁLIDA!')
        sair=str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

    if sair == 'N':
        break

    cont+=1
print('='*30)
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {caro} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {nomeMaisBarato} que custa R$ {maisBarato}!')