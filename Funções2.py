#Interactive help
#help()
help(print)
help(input.__doc__)

#Docstrings
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela <-
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    ->Função Criada por Wollacy Willyan de Carvalho 21/07/2022<-
    """
   
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(0, 100, 10)

help(contador)