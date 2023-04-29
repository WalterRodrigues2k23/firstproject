import time

class Timer:
    def __init__(self, value = 0):
        self.start = time.time()
        self.set(value)
        
    def reset(self):
        self.set(0)
        
    def set(self, value : float):
        self.start = time.time() - value     
        
    def get(self) -> float:
        return time.time() - self.start
    
    def __str__(self):
        value = self.get()
        sec = int(value)
        ms  = int((value - sec) * 1000)
        
        min = int(sec / 60)
        sec -= min * 60
        return str(min)+"m "+str(sec)+"s "+str(ms)+"ms"

