meta = valorFaltante = 1000
investir = 100
valorInvestido = 0

print(f'\033[7;33;44mMETA - R$ {meta:.2f}\033[m')

while True:
    if meta == valorInvestido:
        print('\033[30;42mMeta alcançada com sucesso!\033[m')
        break
    else:
        valorInvestido += investir
        valorFaltante = meta - valorInvestido
        print(f'\033[0;30;41mValor investido R$ {valorInvestido:.2f}, falta R$ {valorFaltante:.2f} para atingir a meta!\033[m')