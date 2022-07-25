def fatorial(valor, show='False'):
    """
    -> FUNÇÃO PARA CALCULAR O FATORIAL <-
    :1º param: valor: Recebe o valor para calcular o valor fatorial.(Parâmetro obrigatório)
    :2º param: show: Recebe o valor 'True' ou 'False', indicando se mostra ou não o cálculo do fatorial.(Parâmetro opcional, Default = False)
    """
    total = 1
    for num in range(valor, 0, -1):
        total *= num
        
        if show == 'True':
            if num > 1:
                print(f'{num} x ', end='')
            else:
                print(f'{num} = ', end='')
        
    print(total)


fatorial(5, show='True')
help(fatorial)