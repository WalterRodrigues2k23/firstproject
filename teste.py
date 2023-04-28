import time

time.sleep(1)
while True:
  input("Enter")
  tempoini = time.time()
  while True:
    input("")
    tempofim = time.time()

    time.perf_counter_ns = tempofim - tempoini
    print(time.perf_counter_ns)