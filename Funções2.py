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

#Parâmetros Opcionais
def somar(a=0, b=0, c=0):
    """
    ->Faz a soma de três valores e mostra na tela<-
    :param a: Primeiro valor - Não Obrigatório
    :param b: Segundo valor - Não Obrigatório
    :param c: Terceiro valor - Não Obrigatório
    :return: Sem retorno
    ->Função Criada por Wollacy Willyan de Carvalho 22/07/2022<-
    """
    
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()

print()

#Retorno
def retSoma(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = retSoma(3, 2, 5)
r2 = retSoma(8, 4)
r3 = retSoma()

print(f'As somas deram {r1}, {r2} e {r3}...')


def fatorial(num=1):
    f = 1
    for c in range(num, 0 , -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os fatoriais são {f1}, {f2} e {f3}...')

def parImpar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um valor: '))

if parImpar(num):
    print('É par!')
else:
    print('É ímpar!')