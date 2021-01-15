## Detector de Palíndromo

frase=str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)

inverso = ''
## inverso = junto[::-1] - Outra forma de mostrar a forma inversa da palavra

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

if junto == inverso:
    print('A frase {} ao contrário é {}. Temos um Palíndromo!'.format(junto, inverso))
else:
    print('A frase {} ao contrário é {}. Não temos um palíndromo'.format(junto, inverso))