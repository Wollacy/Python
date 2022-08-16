import moeda107

n = float(input('Digite um preço: R$'))
metade = moeda107.metade(n)
dobro = moeda107.dobro(n)
aumentar = moeda107.aumentar(n)
diminuir = moeda107.diminuir(n)

print(f'A metade de R${n:.2f} é R${metade:.2f}.')
print(f'O dobro de R${n:.2f} é R${dobro:.2f}.')
print(f'Aumentando 10%, temos R${aumentar:.2f}.')
print(f'Diminuindo 13%, temos R${diminuir:.2f}.')