## Validação de Dados

sexo=str(input('Digite seu sexo (M/F): ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
  sexo=str(input('Sexo inválido! Digite seu sexo (M/F): ')).strip().upper()[0]

print('='*30)
print('Sexo Válido: {}'.format(sexo))