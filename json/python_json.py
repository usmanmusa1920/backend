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
        print('An error occured while clearing screen')
# os_type()
# print()


# loading json from a file
def loading_json_from_file():
    with open('json_file.json') as f:
        file = json.load(f)
        
    print(file['focus'])
    print(file['field'])
    print(file['5g'])
# loading_json_from_file()
# print()


# loading json from a string
def json_from_string():
    json_str = '{"f_name": "Yusuf", "l_name": "Musa", "field": "Health", "focus": "chemistry", "is_talent": true, "city": "zaria", "light": false, "water": true, "5g": null, "name": "kamiński"}'

    json_load = json.loads(json_str)
    print(json_load['focus'])
    print(json_load['field'])
    print(json_load['5g'])
# json_from_string()
# print()


# loading python string dictionary to json
def string_dict_to_json():
    dict_str_1 = {'f_name': 'Yusuf', 'l_name': 'Musa', 'field': 'Health', 'focus': 'chemistry', 'is_talent': True, 'city': 'zaria', 'light': False, 'water': True, '5g': None, 'name': 'kamiński'}

    dict_load = json.dumps(dict_str_1)
    print(dict_load)
# string_dict_to_json()
# print()


# loading python dictionary from a file to json
def json_from_dict():
    dict_str_2 = {'f_name': 'Yusuf', 'l_name': 'Musa', 'field': 'Health', 'focus': 'chemistry', 'is_talent': True, 'city': 'zaria', 'light': False, 'water': True, '5g': None, 'name': 'kamiński'}

    # the below context manager of with will create a file and write a json object in it
    with open('dict_now.txt', 'w', encoding='utf-8') as f:
        json.dump(dict_str_2, f, ensure_ascii=False, indent=8, separators=(',', ': '))

    print(dict_str_2['focus'])
    print(dict_str_2['field'])
    print(dict_str_2['5g'])
json_from_dict()
