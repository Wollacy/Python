
import random
from time import sleep
pc=random.randint(0, 10)

print('Vou pensar em um número entre 0 e 10 tente adivinhar!')
n=int(input('Digite um número: '))

tentativa=1

while n != pc:
    if n > pc:
        print('Menos...')
    else:
        print('Mais...')
    print('')
    n=int(input('Digite novamente: '))
    tentativa += 1

print('='*30)

if tentativa == 1:
    print('Acertou de primeira Miserávi!!!')
elif tentativa >2 and tentativa < 5:
    print('Acertou! Só precisou de {} tentativas!'.format(tentativa))
else:
    print('Até que fim acertou depois de {} tentativas...'.format(tentativa))