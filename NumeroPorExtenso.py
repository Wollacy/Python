## Escreve o número por extenso

lista=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','qunize','dezeseis','dezesete','dezoito','dezenove','vinte')

while True:
    num=int(input('Digite um número entre 0 e 20: '))
    
    if num>=0 and num <=20:
        print(f'Você digitou o numero {lista[num]}')
        break