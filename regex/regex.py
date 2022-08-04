import os
import re

def os_type(n=os.name):
  if os.name == n:
    os.system('clear')
  else:
    os.system('cls')
os_type()

# txt = 'Usman Musa @!./* 4421'
# patn = re.compile(r'[\W\D]')
# n = patn.finditer(txt)

# for i in n:
#     print(i)
# print(txt[0:5])

txt = '''
Mr Usman
Mrs Maryam
Mr. Musa
Mrs. Hafsat
'''

b = input('Enter string: ')
patn = re.compile(re.escape(b))
print(patn)
n = patn.finditer(txt)

for i in n:
    print(i)
    
# print(txt[0:5])


# here try to create a file and give it a name 'number.txt', copy and paste the below code into the file
"""
  661-789-112
  881-999-771
  mooo-gold
  419Game
  000-343-990
  555-555-555
"""

try:
  with open('number.txt', 'r', encoding='utf-8') as f:
    fout = f.read()
    out = re.compile(r'\d{3}(\.|-*-)\d{3}(\.|-)\d{3}')
    g = out.finditer(fout)
    
    for i in g:
      print(i)
except:
  print('We do not find the number file, that we want to capture numbers pattern. Please create it run me again')
