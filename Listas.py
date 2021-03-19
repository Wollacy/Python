## Listas

lista1 = [0,4,5,1,2,7,9,3]
lista2 = ["Olá","Mundo","!"]
lista3 = [0, "Olá", "Biscoito", "Bolacha", 9.99, True]
lista1.append(6)

print(lista1)
print('-='*30)
print(lista3)
print('-='*30)
lista1.sort()
print(lista1)
print('-='*30)
lista1.sort(reverse=True)
print(lista1)
print('-='*30)
print(f'Lista 1 tem {len(lista1)} elementos!')

lista1.insert(2, 8)
print(lista1)

lista1.pop()
print(lista1)

lista1.pop(5)
print(lista1)

lista1.remove(8)
print(lista1)

if "Mundo" in lista3:
  lista3.pop()

print('')

for i in lista1:
  print(i)

print('')

for i in lista2:
  print(i)

print('')

for i in lista3:
  print(i)


valores=[]
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
  print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2,3,4,7]
b = a
b[2] = 8

print(a)
print(b)

c = [1, 2, 3, 4]
d = c[:]
d[2] = 5

print(c)
print(d)