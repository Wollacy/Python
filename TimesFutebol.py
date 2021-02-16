## Tuplas com Times de Futebol

times = ('Internacional','Flamengo','Atlético-MG','São Paulo','Fluminense','Palmeiras','Grêmio','Atlético-PR','Santos','Corinthians','Bragantino','Ceará SC','Atlético GO','Sport Recife','Fortaleza','Bahia','Vasco da Gama','Goiás','Coritiba','Botafogo')

print('-='*50)
print(times)
print('-='*50)
print(f'Os 5 primeiros colocados são: \033[0;32m{times[0:5]}\033[m')
print('-='*50)
print(f'Os 4 últimos colocados são: \033[0;31m{times[-4:]}\033[m')
print('-='*50)
print(f'Os times em ordem alfabética: \033[0;34m{sorted(times)}\033[m')
print('-='*50)
print(f'O Corinthians está ná \033[0;33m{times.index("Corinthians")+1}ª posição\033[m!')
print('-='*50)