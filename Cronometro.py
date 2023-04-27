from time import sleep
import os

def limpar():

    os.system('CLS')

minuto = segundo = milisegundo = 0

print('Informe o tempo do cronômetro:')
print()

mfinal = int(input('Minuto: '))
sfinal = int(input('Segundo: '))
msfinal = int(input('MiliSegundo: '))

while True:

    print(f'{minuto}:{segundo}:{milisegundo}')

    sleep(1)

    milisegundo += 1

    if milisegundo == 1000:
        milisegundo = 0
        segundo += 1

    if segundo == 60:
        segundo = 0
        minuto += 1

    limpar()

    if minuto == mfinal and segundo == sfinal and milisegundo == msfinal:
        break