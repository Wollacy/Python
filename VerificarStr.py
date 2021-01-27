## Verifica Palavra no Nome

nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

## Concatenando Strings

print('-='*30)
print('CONCATENANDO STRINGS')
print('-='*30)

a = 'Wollacy'
b = 'Lilian'
c = 'Augusto'

print(a)
print(b)
print(c)

d = a + ' + ' + b + ' = ' + c

print(d)