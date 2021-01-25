## Progressão Aritmética v2

n=int(input('Digite o primeiro termo da P.A.: '))
r=int(input('Digite a razão da P.A.: '))

print('='*80)
print('Os dez primeiros termos da P.A. começando com o número {} e a razão {} é: '.format(n, r))
print('='*80)

c=0
while c < 10:
  print(n, end=' -> ')
  n+=r
  c += 1
print('Fim!')
print('='*80)