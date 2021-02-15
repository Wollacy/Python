## Aplicativo de Pedidos para Restaurentes

print('Olá ')
print('='*30)
print('SEJA BEM VINDO'.center(30))

sair='N'
tour='A'
contin = 1

while tour != 'S' and tour != 'N':
    tour=str(input('Gostaria de um brve tour pelo nosso sistema? [S/N]')).upper()
    if tour == 'S':
        while contin == 1:
            contin=int(input('Pressione 1 para continuar'))
    elif tour == 'N':
        print('SEGUE O BAILE')
    else:
        print('\033[4;33mResposta inválida! Responda S para SIM e N para NÃO\033[m')

print('*'*30)
print('Então vamos lá...')
print('*'*30)

while sair != 'S':
    escolha=int(input('''
    ===============================
    Escolha a opção desejada!
    [1] Salgados
    [2] Doces
    [3] Bebidas
    [0] Sair
    ===============================
    '''))
    if escolha == 1:
        print('''\033[4;32mSalgados\033[m
        Escolha o item e a quantidade
        =================================
        Cód.    Item            Preço
        =================================
        [ 1] - 
        [ 2]
        [ 3]
        [ 4]
        [ 5]
        [ 6]
        [ 7]
        [ 8]
        [ 9]
        [10]
        ''')
        
    elif escolha == 2:
        print('Doces')
    elif escolha == 0:
        print('Sair')
        sair = 'S'
    else:
        print('\033[0;31mEscolha inválida!\033[m')