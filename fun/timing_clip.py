import time

def count_items(items):
    print('Counting ', end='', flush=True)
    num = 0
    for item in items:
        num += 1
        time.sleep(1)
        print('.', end='', flush=True)
    time.sleep(1)
    print(f'\nThere is {num} items')
    
count_items(['1', '3', '9', '4'])
l = 'I am Usman Musa'

for i in l:
  time.sleep(0.2)
  print(i, end='', flush=True)
print()
