import os
import hashlib
import subprocess as sp
from getpass import getpass

"""This python script is not for hacking but just for making a recursive change of some letters using the .replace() method"""
def os_type(n=os.name):
    if os.name == n:
        try:
            sp.run(['clear'])
        except:
            os.system('clear')
    elif os.name == n:
        try:
            sp.run(['cls'])
        except:
            os.system('cls')
    else:
        try:
            sp.run(['banner', 'who are you'])
        except:
            print('We don\'t know your system!')
os_type()


class shopping_profile:
    def __init__(self, name='', item='', pass1='', pass2=''):
        self.name = name
        self.item = item
        self.pass1 = pass1
        self.pass2 = pass2
        
        while self.name == '' or self.pass1 == '' or self.pass2 == '' or self.pass2 != self.pass1:
            if self.name == '':
                self.name = input('Enter your name: ')
            elif self.item == '':
                self.item = input('Pleas enter an item: ')
            elif self.pass1 == '':
                self.pass1 = getpass('Enter password: ')
            elif self.pass2 == '':
                self.pass2 = getpass('Enter password again: ')
            elif self.pass2 != self.pass1:
                print('Two password didn\'t match enter please enter again!')
                self.pass2 = getpass('Enter password again: ')
            else:
                pass
    
    def info(self):
        hash = str(hashlib.sha256(str.encode(self.pass2)).digest())
        h = str(hashlib.sha256(str.encode(self.pass2)).digest())
        
        #salt = hash.replace('1', '*')
        """
        instead of using the above commented replace method, we can use the for loop below, to handle many replacement at once
        """
        for r in (("1", " .. @ .... @ ..  "), ("0", "   .. @.    .   @ ...   "), ("a", "   .. @.  .@.   .@ ..   "), ("x", ".  @  ....   @     @ ... @  . . @"), ("\\", "   ...  @      .     @ ..   "), (".", ".    ."), ("@", ".  .")):
            hash = hash.replace(*r)
            salt = hash
        return '\n' + h + '\n\n\n' + hash + '\n\n\nHey! ' + self.name + ', you added [' + self.item + '] in your chart, and your shopping secret password is (' + self.pass2 + ') ((' + salt + '))\n\n\n'
    
    
    def file(self):
        with open(self.name+'.txt', 'w') as f:
            f.write(self.info())
        
        return 'Job is done, a file has been created which include your password hash and the information you just entered!'

print(shopping_profile().file())
