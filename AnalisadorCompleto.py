## Analisador Completo

idadetotal=0
menosVinte=0
idadeVelho=0
nomeVelho=''

for c in range(1,5):
    nome=str(input('Digite o {}º nome: '.format(c)))
    idade=int(input('Digite a idade da {}º pessoa: '.format(c)))
    sexo=str(input('Digite o sexo da {}º pessoa: (M/F)'.format(c))).strip()

    print('='*35)
    
    idadetotal += idade

    if sexo in 'Mm' and idade > idadeVelho:
            idadeVelho=idade
            nomeVelho=nome
    if sexo in 'Ff' and idade < 20:
            menosVinte += 1

media = idadetotal/4

print(' ')
print('A média de idade do grupo é de {} anos.'.format(media))
print('='*35)
print('O homem mais velho é {} com {} anos.'.format(nomeVelho,idadeVelho))
print('='*35)
print('No grupo tem {} mulheres com menos de 20 anos.'.format(menosVinte))
print('='*35)