## Análise de Idade - Básico

nome=input('Digite seu nome: ')
print('')
idade=int(input('Olá {}! Digite sua idade: '.format(nome)))
print('')

if idade<=18:
  mensagem="Você é muito novo!"
elif (idade>=18)&(idade<40):
  mensagem="Meia idade!"
else:
  mensagem="Muito velho!"

print(mensagem)