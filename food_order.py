#!bin/usr/python
chart = []


class shopping:
  def __init__(self, name = '', chart = chart, age = '', food = '', region = ''):
    self.chart = chart
    self.name = name
    self.age = age
    self.food = food
    self.region = region
    
    
    while self.name == '' or self.age == '' or self.food == '' or self.region == '':
      if self.name == '':
        self.name = input('Enter your full name: ')
        
      # if no space is in the name, it will show the first alphabet,
      # some asterick and the last alphabet e,g u*************n
      elif not ' ' in self.name:
        print(self.name[0], self.name[1:-1].replace(self.name[1:-1], '*') *  (len(self.name) - 2), self.name[-1], sep='')
        print('\nPlease include last name!')
        self.name = input('Enter your full name: ')
        
      elif self.age == '':
        self.age = input('Enter your age: ')
        
      elif self.food == '':
        self.food = input('Enter your food: ')
        
      else:
        self.region = input('Enter your region: ')
    
    
  def info(self):
      f_name, l_name = self.name.split(' ')
      self.f_name = f_name
      self.l_name = l_name
      return 'Our customer ' + self.l_name + ' ' + self.f_name + ' is going to order a food now.'
  
  
  def add_user(self):
    chart.append(self.food)
    return f'You added {self.food} in the chart for an order!'
  
  
  def __str__(self):
    return self.name
    
    
a = shopping()
b = a.info()
c = a.add_user()


print(b)
print(c)
print(chart)