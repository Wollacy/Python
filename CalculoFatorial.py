## Cálculo Fatorial

from math import factorial

n1=int(input('Digite um número para calcular seu fatorial: '))
f1=factorial(n1)

print('='*35)
print('O fatorial com IMPORT de {} é: {}'.format(n1, f1))
print('='*35)

c = n1
r = 1

print('Calculando {}! com WHILE = '.format(n1), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    r *= c
    c -= 1
print(r)
print('='*35)

f=1
print('Calculando {}! com FOR = '.format(n1), end='')
for i in range(n1, 0, -1):
    print('{}'.format(i), end='')
    print(' X ' if i > 1 else ' = ', end='')
    f *= i
    i -= 1
print(f)
print('='*35)