## Soma Ímpares Múltiplos de Três

s=0
v=0

for n in range(0,500):
  if n %2 != 0 and n %3 == 0:
    s = s + n
    v = v + 1

print('A soma de todos os {} valores solicitados é {}!'.format(v,s))

s=0
v=0

for n in range(1,501,2):
  if n %3 == 0:
    s += n
    v += 1

print('A soma de todos os {} valores solicitados é {}!'.format(v,s))