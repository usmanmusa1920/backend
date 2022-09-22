import threading
import time

threads = []
t1 = time.perf_counter()

def info(name):
  print(f"{name}, it's sleeping for a second for loop {name} now!")
  time.sleep(1)
    

for _ in range(1, 60):
  t = threading.Thread(target=info, args=['Usman'])
  t.start()
  threads.append(t)

for t in threads:
  t.join()
#info('Usman')
t2 = time.perf_counter()
#time.sleep(3)
print(f"Finished in {t2 - t1} seconds")
print()





#class sample(threading.Thread):
#  def run(self):
#    print(f"{self.getName()} started!")
#    time.sleep(1)
#    print(f"{self.getName()} finished!")
#    print()
#
#def getCls():
#  for _ in range(5):
#    myThread = sample(name = f"Thread - {_}")  
#    myThread.start()
#    time.sleep(.9)
    
#t1 = time.perf_counter()
#getCls()
#t2 = time.perf_counter()
#time.sleep(3)
#print(f"Finished in {t2 - t1} seconds")
#print()







