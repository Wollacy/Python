## Sequência de Fibonacci

n=int(input('Quantos termos você quer mostrar? '))
c = s = ant = 0

while c < n :
    if c < 2:
        print(s, end=' -> ')
        s = 1
    else:
        prox = ant + s
        print(prox, end=' -> ')
        ant = s
        s = prox
    c += 1
print('FIM')