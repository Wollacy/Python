## Progressão Aritmética

n=int(input('Digite o primeiro termo da P.A.: '))
r=int(input('Digite a razão da P.A.: '))

print('='*80)
print('Os dez primeiros termos da P.A. começando com o número {} e a razão {} é: '.format(n, r))
print('='*80)

for cont in range(1,11):
  print(n, end=' -> ')
  n+=r
print('Fim!')
print('='*80)