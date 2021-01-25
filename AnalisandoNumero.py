## Analisando Números

from time import sleep 

n1 = int(input('Digite um número: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print('Analisando o número {}'.format(n1))
print('Aguarde...')
sleep(1)
print('Unidade {}'.format(u))
sleep(0.5)
print('Dezena {}'.format(d))
sleep(0.5)
print('Centena {}'.format(c))
sleep(0.5)
print('Milhar {}'.format(m))