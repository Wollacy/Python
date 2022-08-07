import uteis

n = int(input('Digite um preço: R$'))
metade = uteis.metade(n)
dobro = uteis.dobro(n)
aumentar = uteis.aumentar(n)
diminuir = uteis.diminuir(n)

print(f'A metade de R${n:.2f} é R${metade:.2f}.')
print(f'O dobro de R${n:.2f} é R${dobro:.2f}.')
print(f'Aumentando 10%, temos R${aumentar:.2f}.')
print(f'Diminuindo 13%, temos R${diminuir:.2f}.')