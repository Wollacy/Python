## While com Break

n = s = c = 0

while True:
    n=int(input('Digite um número [999 para sair]: '))
    if n == 999:
        break
    s += n
    c += 1
print('*'*30)
print(f'A soma entre os {c} valores digitados é de {s}!')