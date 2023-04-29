import time

def print_time(total_seconds):
    total_mins = total_seconds / 60
    seconds = int(total_seconds % 60)
    hours = int(total_mins / 60)
    mins = int(total_mins % 60)
    print('Tempo total: {} horas: {} minutos: {} segundos.'.format(hours(00), mins(00), seconds(00),))

input('Aperte ENTER para começar: ')
start_time = time.time()

print('Cronometro ativo')

input('Aperte ENTER para parar: ')
stop_time = time.time()

print_time(stop_time - start_time)