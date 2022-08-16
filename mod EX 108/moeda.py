def aumentar(n):
    p = (n * 10) / 100
    aumentar = p + n
    return aumentar


def diminuir(n):
    p = (n * 13) / 100
    diminuir = n - p
    return diminuir


def dobro(n):
    dobro = n * 2
    return dobro


def metade(n):
    metade = n / 2
    return metade

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')