import json
import os
import time



def os_type(n=os.name):
  if os.name == n: # for linux and unix
    os.system('clear')
    time.sleep(0.05)
  elif os.name == n: # for windows
    os.system('cls')
  else:
    print('Anerror occured while clearing screen')
os_type()


# loading json from a file
with open('json_file.json') as f:
  file = json.load(f)
  
# print(file['focus'])
# print(file['field'])
# print(file['5g'])



# loading json from a string
json_str = '{"f_name": "Yusuf", "l_name": "Musa", "field": "Health", "focus": "chemistry", "is_talent": true, "city": "zaria", "light": false, "water": true, "5g": null, "name": "kamiński"}'

json_load = json.loads(json_str)
# print(json_load['focus'])
# print(json_load['field'])
# print(json_load['5g'])



# loading python string dictionary to json
dict_str_1 = {'f_name': 'Yusuf', 'l_name': 'Musa', 'field': 'Health', 'focus': 'chemistry', 'is_talent': True, 'city': 'zaria', 'light': False, 'water': True, '5g': None, 'name': 'kamiński'}

dict_load = json.dumps(dict_str_1)
# print(dict_load)



# loading python dictionary from a file to json
dict_str_2 = {'f_name': 'Yusuf', 'l_name': 'Musa', 'field': 'Health', 'focus': 'chemistry', 'is_talent': True, 'city': 'zaria', 'light': False, 'water': True, '5g': None, 'name': 'kamiński'}

with open('dict_now.txt', 'w', encoding='utf-8') as f:
  json.dump('dict_now.txt', f, ensure_ascii=False, indent=10, separators=(',', ': '))
  # json.dump.close()
  
# print(file['focus'])
# print(file['field'])
# print(file['5g'])
