import os
import re
from getpass import getpass
from datetime import datetime

os_name = os.name

if os_name == 'posix':
    os.system('clear')
elif os_name == 'nt':
    os.system('cls')
else:
    print('We don\'t know your system')


class person:
    def __init__(self,
        first = '',
        last = '',
        gender = '',
        birthday = '',
        phone = '',
        passwd_1 = '',
        passwd_2 = '',
    ):
        self.first  = first
        self.last = last
        self.gender = gender
        self.birthday = birthday
        self.phone = phone
        self.passwd_1 = passwd_1
        self.passwd_2 = passwd_2
        
        while self.first == '':
            self.first = input('First name: ')
        else:
            self.first = self.first[0].upper() + self.first[1:].lower()
        while self.last == '':
            self.last = input('Last name: ')
        else:
            self.last = self.last[0].upper() + self.last[1:].lower()
        while self.gender != 'female' and self.gender != 'male':
            print('Note your gender must be either "female" or "male"')
            self.gender = input('\tEnter your gender: ')
        while self.birthday == '' or len(self.birthday) < 8 or len(self.birthday) > 8:
            if self.birthday == '':
                self.birthday = input('Enter your birthday: ').replace(' ', '')
            elif len(self.birthday) < 8 or len(self.birthday) > 8:
                print('\nYour date of birth must be 8 digits long (dd mm yyyy), include leading zero for whole number, e.g for january don\'t use \'1\' only instead use \'01\', likewise also for the days.')
                self.birthday = input('Enterd your birthday: ').replace(' ', '')
            pass
        while self.phone == '':
            self.phone = input('Phone number: ')
        while self.passwd_1 == '' or len(self.passwd_1) < 6 or self.passwd_2 == '' or len(self.passwd_2) < 6 or self.passwd_2 != self.passwd_1:
            if self.passwd_1 == '':
                self.passwd_1 = getpass('Enter password: ')
            elif len(self.passwd_1) < 6:
                print('\nThe password is too short, at least 6 character!\n')
                self.passwd_1 = getpass('Enter password: ')
            elif self.passwd_2 == '':
                self.passwd_2 = getpass('Enter password (again): ')
            elif len(self.passwd_2) < 6:
                print('\nThe confirm password must be thesame with the one you just entered\n')
                self.passwd_2 = getpass('Enter password (again): ')
            elif self.passwd_2 != self.passwd_1:
                print('\nYour password did not match\n')
                self.passwd_1 = getpass('Enter password: ')
                self.passwd_2 = getpass('Enter password (again): ')
            pass
        

    # this method will be saved in the <user>@sqlite.txt file
    def user_info(self):
        if self.gender == 'female':
            return 'The person with this profile she is ' + self.first + ' ' + self.last + ', she was born in ' + self.birthday[0:2] + ' ' + self.birthday[2:-4] + ' ' + self.birthday[-4:] + ', her gender is ' + self.gender + ', her phone number is ' +  self.phone[0:4] + ' ' + self.phone[4:-4] + ' ' + self.phone[-4:] +  ', and her password is =>> ' + self.passwd_2
        return 'The person with this profile he is ' + self.first + ' ' + self.last + ', he was born in ' + self.birthday[0:2] + ' ' + self.birthday[2:-4] + ' ' + self.birthday[-4:] + ', his gender is ' + self.gender + ', his phone number is ' +  self.phone[0:4] + ' ' + self.phone[4:-4] + ' ' + self.phone[-4:] +  ', and his password is =>> \'' + self.passwd_2 + '\''
              
                
    # This method create the file  <user>@sqlite.txt
    def account_name(self):
        return self.first + self.last + '@sqlite.txt'
    
        # Here we check to see if a file with the user name already exist, if it exist it will ask him for the password, that he setup when creating it and if it match it he has the right to modify the file, ELSE he will be thrown away
        # But in the case if the file does not exist it will create a new one for him
    
    
    def file_create(self):
        file_user = a.account_name()
        
        if os.path.exists(file_user):
            print('\nSome one already owned this  file (' + file_user + ')')
            owner = input('Are you the owner of the file? (' + file_user + ') yes/no  or y/n: ')
            
            while owner != 'yes' and owner != 'y' and owner != 'no' and owner != 'n':
                owner = input('Are you the owner of the file? (' + file_user + ') yes/no  or y/n: ')
            if owner == 'yes' or owner == 'y':
                ask_file_replace = input('Do you want to replace your file with new one? yes/no  or y/n: ')
                        
                while ask_file_replace != 'yes' and ask_file_replace != 'no' and ask_file_replace != 'y' and ask_file_replace != 'n':
                    ask_file_replace = input('Do you want to replace your file with new one? yes/no  or y/n: ')
                if ask_file_replace == 'yes' or ask_file_replace == 'y':
                    open_file = open(file_user, 'r', encoding='utf-8')
                    file_read = open_file.read()
                    pass_ask = input('Enter your password to confirm: ')
                    search_pass = re.compile(re.escape(pass_ask))
                    pattrn_srch = search_pass.search(file_read)
                    
                    while pass_ask == '' or pass_ask == 'quit':
                        if pass_ask == 'quit':
                            return 'You quited your file overwrite'
                        pass_ask = input('Enter your password to confirm, it cant be empty!: ')
                    
                    # while pass_ask != pattrn_srch:
                    #     pass_ask = input('Enter your password to confirm: ')
                    
                    if pattrn_srch:
                        new_file = open(file_user, 'w')
                        new_file.write(self.user_info())
                        new_file.close()
                        return 'Your previous file has been renewed! (' + file_user + ')\n'
                    return 'The password you enter is not correct try again later!'
                return 'Weldone your file has no any new update!'
            return 'We are sorry, be patient, please create a different file name since (' + file_user + ') has been taken by another user.\n'
               
        """ This is where it will create a new file if the user\'s file does not exist """
        
        new_file = open(file_user, 'w')
        new_file.write(self.user_info())
        new_file.close()
        return 'Your new file has been created! (' + file_user + ')'
    
    
    """ this method will check to see if the user birthday is equal to the current date, and if it is it will welcome hime with happy birthday message """
    def happ_birthday(self):
        
        day = datetime.today().day
        month = datetime.today().month
        year = datetime.today().year

        current_str_1 = str(day) + str(month) + str(year)
        
        current_str_day = str(0) + str(day)
        current_str_2 = current_str_day + str(month) + str(year)

        current_day_str = current_str_2[0:2]
        current_month_str = current_str_2[2:4]
        current_year_str = current_str_2[4:]

        current_day_int = int(current_day_str)
        current_month_int = int(current_month_str)
        current_year_int = int(current_year_str)
        
        DOB_str = str(self.birthday)
        
        DOB_day_str = DOB_str[0:2]
        DOB_month_str = DOB_str[2:4]
        DOB_year_str = DOB_str[4:]
        
        DOB_day_int = int(DOB_day_str)
        DOB_month_int = int(DOB_month_str)
        DOB_year_int = int(DOB_year_str)
        
        
        if len(str(day)) == 1:
            if len(str(month)) == 1:
                current_str_month = str(0) + str(month)
                print(current_str_month)
                
                if DOB_day_str == current_str_day and DOB_month_str == current_str_month:
                    return 'we wish you a happy birthday1'
                elif int(current_str_month) - DOB_month_int == 3:
                    return 'Hi ' + self.first + ', in an upcoming 3 month you will be in a new world1'
                elif int(current_str_month) - DOB_month_int == 2:
                    return 'Hi ' + self.first + ', in an upcoming 2 month you will be in a new world1'
                else:
                    pass
            else:
                current_month_str = current_str_2[2:4]
                if DOB_day_str == current_day_str and DOB_month_str == current_month_str:
                    return 'we wish you a happy birthday2'
                elif current_month_int - DOB_month_int == 3:
                    return 'Hi ' + self.first + ', we whish you a happy birthday and more grace year ahead with prosperity.2'
                elif current_month_int - DOB_month_int == 2:
                    return 'Hi ' + self.first + ', we whish you a happy birthday and more grace year ahead with prosperity.3'
                pass
        else:
            current_str_day = str(day)
            if len(str(month)) == 1:
                current_str_month = str(0) + str(month)
            else:
                pass
                
        
    def __str__(self):
        if self.gender == 'female':
            return 'The person with this profile she is ' + self.first + ' ' + self.last + ' and her password is "' + self.passwd_2 + '"'
        return 'The person with this profile he is ' + self.first + ' ' + self.last + ' and his password is "' + self.passwd_2 + '"'
    
a = person()

print(a.file_create())
print(a.happ_birthday())
