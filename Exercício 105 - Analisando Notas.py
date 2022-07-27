def notas(*n, sit=False):
    """
    -> FUNÇÃO PARA ANALISAR NOTAS E SITUAÇÕES <-
    :param n: Informa as notas do aluno
    :param sit: Informar a situação do aluno 'True' ou 'False'(Default: False)
    :return: Retorna um dicionário com o total de notas informados, a maior nota, a menor nota, a média e a situação.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

resp = notas(3, 0, 1.0, sit=True)
print(resp)
help(notas)