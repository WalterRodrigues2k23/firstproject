import time


def print_time(total_seconds):
    total_mins = total_seconds / 60
    seconds = int(total_seconds % 60)
    hours = int(total_mins / 60)
    mins = int(total_mins % 60)
    print('Tempo total: {:02d} h : {:02d} m : {:02d} s. {} '.format(hours, mins, seconds, mlsec))

if input('Aperte ENTER para começar a inspeção: ') == True:
   input('Aperte ENTER para começar a inspeção: ')
time.sleep(15)
input('Aperte ENTER para começar: ')
tempoini = time.time()
mlsec = repr(tempoini).split('.')[1][:3]
print('Cronometro ativo')

input('Aperte ENTER para parar: ')
tempofim = time.time() - tempoini

print_time(tempofim)