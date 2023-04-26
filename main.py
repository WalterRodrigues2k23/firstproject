import time

starttime = time.time()
lasttime = starttime
lapnum = 1
value = ""
  
print("Aperte ENTER Para gravar o seu tempo.\n Aperte Q e aperte ENTER para finalizar o seu treino.")
  
while value.lower() != "q":
              
    # Input for the ENTER key press
    value = input()
  
    # The current lap-time
    laptime = round((time.time() - lasttime), 2)
  
    # Printing the lap number, lap-time, and total time
    print("Tempo No. "+str(lapnum))
    print("Seu tempo foi: "+str(laptime), "segundos.")
            
    print("-"*20)
  
    # Updating the previous total time and lap number
    lasttime = time.time()
    lapnum += 1
  
print("Treinamento concluído!")
