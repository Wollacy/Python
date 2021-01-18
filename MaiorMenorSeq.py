## Maior e Menor da Sequência

for c in range(1,6):
  peso=float(input('Digite o peso da {}ª pessoa: '.format(c)))
  
  if c == 1:
      leve=peso
      pesado=peso

  if peso <= leve:
    leve = peso

  if peso >= pesado:
    pesado = peso

print('='*30)
print('O mais pesado foi {}Kg'.format(pesado))
print('O mais leve foi {}Kg'.format(leve))