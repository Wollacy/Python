def aumentar(preco=0, taxa=0, formato=False):
    p = (preco * taxa) / 100
    aumentar = p + preco
    return aumentar if formato is False else moeda(aumentar)


def diminuir(preco=0, taxa=0, formato=False):
    p = (preco * taxa) / 100
    diminuir = preco - p
    return diminuir if formato is False else moeda(diminuir)


def dobro(preco, formato=False):
    dobro = preco * 2
    return dobro if formato is False else moeda(dobro)


def metade(preco, formato=False):
    metade = preco / 2
    return metade if formato is False else moeda(metade)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0, aumento=10, reducao=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{moeda(preco):>15}')
    print(f'Metade do Preço: \t{metade(preco, True):>15}')
    print(f'Dobro do Preço: \t{dobro(preco, True):>15}')
    print(f'Com {aumento}% de aumento: \t{aumentar(preco, aumento, True):>15}')
    print(f'Com {reducao}% de redução: \t{diminuir(preco, reducao, True):>15}')
    print('-'*40)