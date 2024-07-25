import hashlib


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)
    
    
    
class Man:
    def __init__(self, yname, zname):
        self.yname = yname
        self.zname = zname
    def printname(self):
        print(self.yname, self.zname)

        
class Student(Person, Man):
    def __init__(self, fname, lname, yname, zname, year):
    # super().__init__(fname, lname)
        Person.__init__(self, fname, lname)
        Man.__init__(self, yname, zname)
        self.grad = year
        
    @property
    def welcome(self):
        return f"Welcome, {self.fname} {self.lname} to the class of {self.grad}"
    
    def secret(self):
        with open(self.fname+self.lname+'_id_rsa.txt', 'w') as f_1:
            f_1.write(self.welcome)
      
        with open(self.fname+self.lname+'_id_rsa.pub', 'w') as f_1:
            hh = self.welcome
            for k in 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890':
            # for i in ([' ', '@@'], ['a', '##'], ['o', '^&&^'], ['@', '.'], ['#', '.'], ['&', '.'], ['^', '.'], ['s', '.'], ['m', '.'], [k, '.']):
                try:
                    kk = k.upper()
                except:
                    pass
                for i in ([k, '.'],):
                    hh = hh.replace(*i)
            f_1.write(hh)
    
    with open(self.fname+self.lname+'_id_rsa.pub') as t:
        print(t.read())
        

def info(*args, **kwargs):
    print(*args)
    return f'**kwargs'


x = Person("John", "Doe")
x.printname()

x = Man("Baby", "Boy")
x.printname()

y = Student('Usman', 'Musa', 'Yname', 'Zname', 2021)
print(y.welcome)
y.secret()

#print(help(Student))
  
info('eee', 'ppp', a='man', b='girl')
