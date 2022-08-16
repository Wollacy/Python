import moeda

n = float(input('Digite um preço: R$'))

print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}.')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}.')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(n))}.')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(n))}.')