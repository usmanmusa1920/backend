import os
import random
import datetime
import calendar


# clearing screen
os.system('clear')


n=int(input('num: '))
lst = ['mango', 'appale', 'orange', 'mango', 'beans', 'rice', 'yam', 'mango', 'cassava']

while n < 10:
  print('The number is not close to 10')
  n=int(input('num again: '))
else:
  print()
  print('The original list is:\n', lst)
  
  print()
  random.shuffle(lst)
  print('The list has been shuffled below:')
  print(lst)
  
  print()
  print('We randomly choose from the list, the choose is ==>', random.choice(lst))
  
  print()
  print('We found', lst.count('mango'), 'repeated \'mango\' in the list')
  
  print()
  print('Today\'s ', datetime.datetime.today())
  
  print()
  print('Below is a calendar:')
  print(calendar.month(2022,8,3))
