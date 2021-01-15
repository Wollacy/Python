## Soma dos Pares

s=0
c=0

for n in range(1,7):
  v=int(input('Digite o {}º número: '.format(n)))
  if v %2 == 0:
    s += v
    c += 1
print('Você informou {} números pares. A soma é: {}'.format(c, s))