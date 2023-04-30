import time
import keyboard

tempo_total = 15
tempo_atual = 0

def print_time(total_seconds):
    global mlsec
    mlsec = repr(time.time()).split('.')[1][:3]
    total_mins = total_seconds / 60
    seconds = int(total_seconds % 60)
    hours = int(total_mins / 60)
    mins = int(total_mins % 60)
    print('\rTempo total: {:02d} h : {:02d} m : {:02d} s. {} '.format(hours, mins, seconds, mlsec), end='')

print('Aperte Espaço para começar a inspeção: ')
keyboard.wait('space')
while tempo_atual < tempo_total:
    tempo_restante = tempo_total - tempo_atual
    print('\r{} segundos'.format(tempo_restante), end='')
    time.sleep(1)
    tempo_atual += 1
    if keyboard.is_pressed('space'):
        pass
        
if tempo_atual >= tempo_total:
    tempoini = time.time()
    mlsec = repr(tempoini).split('.')[1][:3]

    while True:
        print_time(time.time() - tempoini)
        if keyboard.is_pressed('space'):
            break

    tempofim = time.time() - tempoini
    print_time(tempofim)
    print('Parabéns!')