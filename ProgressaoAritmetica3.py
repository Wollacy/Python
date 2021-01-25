## Progressão Aritmética v2

n=int(input('Digite o primeiro termo da P.A.: '))
r=int(input('Digite a razão da P.A.: '))

print('='*80)
print('Os dez primeiros termos da P.A. começando com o número {} e a razão {} é: '.format(n, r))
print('='*80)

c = cont = 0
t = 10

while t != 0:
    while c < t:
        print(n, end=' -> ')
        n+=r
        c += 1
    print(' Pausa ')
    cont += t
    t=int(input('Quantos termos você quer mostrar a mais? '))
    c = 0

print('Progressão finalizada com {} termos mostrados.'.format(cont))
print('Fim!')
print('='*80)