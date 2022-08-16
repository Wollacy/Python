def aumentar(preco=0, taxa=0, formato=False):
    p = (preco * taxa) / 100
    aumentar = p + preco
    return aumentar if formato is False else moeda(preco)


def diminuir(preco=0, taxa=0, formato=False):
    p = (preco * taxa) / 100
    diminuir = preco - p
    return diminuir if formato is False else moeda(preco)


def dobro(preco, formato=False):
    dobro = preco * 2
    return dobro if formato is False else moeda(preco)


def metade(preco, formato=False):
    metade = preco / 2
    return metade if formato is False else moeda(preco)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')