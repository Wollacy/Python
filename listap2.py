teste = list()
teste.append('Wollacy')
teste.append(32)

galera = list()
galera.append(teste[:])

teste[0]='Lilian'
teste[1]=26

galera.append(teste[:])

print(galera)

galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2)

for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade!')

galera3 = list()
dado = list()

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear()

totmai = 0
totmen = 0

for p in galera3:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade!')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores!')