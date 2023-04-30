#https://stackoverflow.com/questions/6677332/using-f-with-strftime-in-python-to-get-microseconds/41679167#41679167

import time
# Get current timestamp
input('Aperte ENTER para começar: ')
time.sleep(3)
i = time.time()
now = time.time() - i

# Get miliseconds
mlsec = repr(now).split('.')[1][:3]
input('Aperte ENTER para parar: ')
# Get your required timestamp string
print (time.strftime(" %H:%M:%S.{}".format(mlsec)))