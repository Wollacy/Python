## Programa criado para sorteio do chá rifa do Agusto

import random
from time import sleep

lista=['1-Livia','2-Jenifer','4-Juce','5-Michelli','7-Camila','8-Deisy','9-Jenifer','13-Cristiane','14-Amanda(Thamy)','15-Juce','16-Philipp','17-Du','18-Tânia(Mãe)',
       '20-Liciane','21-Sarah','22-Juce','24-Josi','25-Leda','26-Thaynara','27-Juce','29-Iane','30-Laise','31-tia Cátia','35-Amanda','36-Isabel','37-Thamy',
       '38-Camila(Jonathan)','39-Marli','42-Jane','43-Nana','44-Mara','45-Lizana','46-Dada','47-Cátia(Carlyles)','49-Benjamim','50-João']
for i in lista:
  print(i)

escolhido = random.choice(lista)
print('='*25)
print('O número sorteado é........')
sleep(3)

print('='*25)
print('\033[1;33;41m{}\033[0m'.format(escolhido))
print('='*25)