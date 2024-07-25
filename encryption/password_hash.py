import hashlib
import os
import random
import base64


token_1 = 'abcdefghijklmnopqrstuvwxyz'
token_2 = token_1.upper()
token_3 = '0123456789'
token_4 = '[]{}()*;/,_-'
token_5 = token_1 + token_2 + token_3 + token_4


shuf_lst = list(token_5)
random.shuffle(shuf_lst)
# print(token_5, '\n', ''.join(shuf_lst))


salt = "".join(random.sample(token_5 * 2, random.randint(32, 64))).encode('utf-8')
itter = random.randrange(260000, 400000, 20)


password = input('Enter a password: ')
while password == '' or password == ' ':
    if password == ' ':
        print('\nPassword can\'t be empty space')
    password = input('Please enter a password: ')

key = hashlib.pbkdf2_hmac(
    'sha256', # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt, # the salt
    itter, # iteration number
    dklen=128 # Get a 128 byte key
)


# concatenating our salt and our key
storage = salt + key

salt_from_storage = storage[:len(salt)] # slicing salt from storage
key_from_storage = storage[len(salt):] # slicing key from storage


# encoding our storage using base64 encode to avoid data corruption
b64h = base64.b64encode(storage).decode("ascii").strip()
print('This is b64h:\n', b64h, sep='')


# hashing our encoded storage to mask against data breach
h_val = hashlib.sha256(str.encode(str(b64h))).hexdigest()
print('\nThis is the hashlib:\n', h_val, sep='')


# backup code for a user
print('\nThese are your 5 backup code:')
for i in range(5):
    j = " ".join(random.sample(token_3*3,9))
    lst = list(j)
    lst[1] = ''
    lst[3] = ''
    lst[7] = ''
    lst[9] = ''
    lst[13] = ''
    lst[15] = ''
    print(' ', ''.join(lst))


print('\nYour API token is:\n', ''.join(random.sample(token_5*100, random.randrange(900, 1000, 100))), sep='')

print(end='\n')
print("\nThe salt is:\n", salt, sep='')
print("\nThe itteration is:\n", itter, sep='')
print("\nThe key is:\n", key, sep='')
print("\nThe storage is:\n", storage, sep='')
print("\nThe salt from storage is\n", salt_from_storage, sep='')
print("\nThe key from storage is:\n", key_from_storage, sep='')
