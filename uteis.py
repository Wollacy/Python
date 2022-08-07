def fatorial(n):
    f=1
    for c in range(1, n+1):
        f *= c
    return f

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