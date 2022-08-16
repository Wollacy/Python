import moeda108

n = float(input('Digite um preço: R$'))

print(f'A metade de {moeda108.moeda(n)} é {moeda108.moeda(moeda108.metade(n))}.')
print(f'O dobro de {moeda108.moeda(n)} é {moeda108.moeda(moeda108.dobro(n))}.')
print(f'Aumentando 10%, temos {moeda108.moeda(moeda108.aumentar(n))}.')
print(f'Diminuindo 13%, temos {moeda108.moeda(moeda108.diminuir(n))}.')