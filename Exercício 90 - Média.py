aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do aluno {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado!'
elif aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado!'
else:
    aluno['situacao'] = 'Em Recuperação!'

print('*=' *20)
for k, v in aluno.items():
    print(f' - {k} é igual à {v}!')