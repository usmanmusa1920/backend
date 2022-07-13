import os
import csv
import time
import random


lst = []

def quiz():
  for i in range(100):
    print('Column ' + str(random.randint(1,3)) + ' line ' + str(random.randint(1,15)) + ' the person in the ' + str(random.randint(1,4)) )
    name = input('Enter person name: ')
    while name == '' or name == ' ':
      name = input('Enter host name please: ')
    t = random.randint(1, 3)
    print(name + ', you have ' + str(t) + ' seconds only!')
    time.sleep(t)
    print()
    rank = 1
    
    lst.append(name)
    print(lst)
    
    ans = input('Do you want to quit the quiz? y/n: ')
    if ans == 'y':
      print('Program finished')
      position = 1+2+3/100
      r_ans = input('Do you want a copy of the results in csv? y/n: ')
      if r_ans == 'y':
        with open(name + '.csv', 'w') as f_rslt:
          csv.write_row(['Name', 'Rank', 'Position'])
          for i in lst:
            csv.write_row([name, rank, position])
      elif r_ans == 'n':
        pass
      else:
        r_ans = input('Do you want a copy of the results in csv? y/n: ')
        
    elif ans == 'n':
      print('Ok, we contineu!')
      continue
      
    while ans != 'y' or ans != 'n':
      ans = input('Do you want to quit the quiz? y/n: ')
      
      
      
quiz()
