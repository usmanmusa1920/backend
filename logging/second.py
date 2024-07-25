import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#when we did not use the logger variable in the basicConfig class (for kwargs, e.g logger.INFO instead logging.INFO) it will use the default one because it is in heirachey

formatter = logging.Formatter(' [+] %(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('second.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

#logging.basicConfig(level=logger.INFO, format=' [+] %(asctime)s:%(levelname)s:%(message)s')

class student:
    def __init__(self, first: 'first name', last) -> 'Normal':
        self.first = first
        self.last = last
        
        print(f"New student: {self.fullname} - {self.email}")
        
    def info(self: bool) -> 'hh':
        return 'Wow it is annotation'
        
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    def __str__(self: False) -> None:
        return 'True'
    

s1 = student('Usman', 'Musa')
s2 = student('Aliyu', 'Sani')
s3 = student('Muhammad', 'Umar')

logging.info(s1)
logging.info(s2)
logging.info(s3)
#print(s1.info.__annotations__)
#print(s1.__str__.__annotations__)
#print(s1.__init__.__annotations__)
logger.info(s1.info())
