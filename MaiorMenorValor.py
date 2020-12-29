## Maior e Menor valor

n1 = int(input('Digite o primeiro valor: '))
maior=n1
menor=n1

n2 = int(input('Digite o segundo valor: '))
if n2 > n1:
  maior = n2
if n2 < n1:
  menor = n2

n3 = int(input('Digite o terceiro valor: '))
if n3 > maior:
  maior=n3
if n3 < menor:
  menor = n3

print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))