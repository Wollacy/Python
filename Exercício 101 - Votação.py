def voto(anoNascimento):
    from datetime import date

    anoAtual = date.today().year
    idade = anoAtual - anoNascimento

    if idade < 16:
        return f'Com {idade} anos o voto NÃO É PERMITIDO'
    elif idade > 16 and idade < 18:
        return f'Com {idade} anos o voto É OPCIONAL'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos o voto É OBRIGATÓRIO'
    else:
        return f'Com {idade} anos o voto É OPCIONAL'


anoNascimento = int(input('Digite o ano de nascimento: '))
print(voto(anoNascimento))