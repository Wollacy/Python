#dados = dict()
#dados = {'nome':'Wollacy', 'idade':32}

#dados['sexo']='M'

#print(dados.items())
#print(dados.values())
#print(dados.keys())

pessoas = {'nome':'Wollacy', 'sexo':'M', 'idade':32}
print(f'O {pessoas["nome"]}, tem {pessoas["idade"]} anos!')

del pessoas['sexo']
pessoas['peso'] = 71.5
pessoas['sexo'] = 'M'
for k, v in pessoas.items():
    print(f'{k} = {v}')

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))

    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()