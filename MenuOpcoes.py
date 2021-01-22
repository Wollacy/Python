## Criando um Menu de Opções

escolha=4

while escolha != 5:
    if escolha == 4:
        n1=int(input('Digite o primeiro valor: '))
        n2=int(input('Digite o segundo valor: '))
    escolha=int(input('''
    ============================================
    Qual a Operação que você deseja realizar?
    ============================================
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
    =============================================
    '''))
    if escolha == 1:
        resultado = n1 + n2
        print('A soma entre {} e {} é : {}'.format(n1, n2, resultado))
    elif escolha == 2:
        resultado = n1 * n2
        print('A multiplicação entre {} e {} é : {}'.format(n1, n2, resultado))
    elif escolha == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é : {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('O maior número entre {} e {} é : {}'.format(n1, n2, n2))
        else:
            print('Os números {} e {} são iguais!'.format(n1, n2))
    elif escolha == 5:
        print('='*60)
    else:
        print('='*60)
        print('Escolha inválida!')
        print('='*60)
        
print('Fim do Programa! Até mais...')
print('='*60)