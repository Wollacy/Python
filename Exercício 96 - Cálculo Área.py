def area(largura, comprimento):
    vlrArea = largura * comprimento

    print(f'A área de um terreno {largura}X{comprimento} é de {vlrArea}m²!')


print(f'{"Controle de Terrenos":^35}')
print('-='*20)
print()

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

area(largura, comprimento)