# a simple program for knowing whether some one is a female or male

class person:
  def __init__(self, first, gender, body=False):
    self.first = first
    self.gender = gender
    self.body = body
    
  def pd(self):
    if self.gender == "m" or self.gender == "male":
      return "My name is " + self.first + " and I am male"
    elif self.gender == "f" or self.gender == "female":
      return "My name is " + self.first + " and I am female"
    else:
      return "My name is " + self.first + " and I am unknown in gender"
   
#      inheritance
class voice(person):
      def __init__(self, first = input('What is your name? '), gender = input('What is your gender m or f? '), body=None, voice=None):
        super().__init__(first, gender, body)
        self.voice = voice
        
      def pvoice(self):
        if self.gender == "f" or self.gender == "female":
          return self.first + ' is a female, her voice is sweet'
        elif self.gender == "m" or self.gender == "male":
          return self.first + ' is a male, his voice is bitter'
        else:
          return self.first + ' we do not know the state of your voice'
      
p = voice()
print(p.pvoice())
