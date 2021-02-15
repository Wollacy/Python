## Aula de Tuplas

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(lanche)
print('-='*30)
print(lanche[1])
print('-='*30)
print(lanche[1:3])
print('-='*30)
print(lanche[:2])
print('-='*30)
print(lanche[-2])
print('-='*30)
for comida in lanche:
    print(f'Vou comer {comida}')
print('-='*30)
for cont in range(0, len(lanche)):
    print(f'Lanche {cont} - {lanche[cont]}')
print('-='*30)
for pos, comida in enumerate(lanche):
    print(f'Lanche {comida} na posição {pos}')
print('-='*30)