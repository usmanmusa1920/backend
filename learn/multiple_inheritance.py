
# this program entails how to use/call super class init, in different way
#     using:
#         super().__init__()
#         <class_name>.__init__(), and

#         super(department, self).__init__(faculty_name, dean) # for faculty 
#         super(faculty, self).__init__(faculty_name, dean) # for house


class house:
  def __init__(self, house_name, dean):
    self.house_name = house_name
    self.dean = dean
    
  def house_info(self, age=input('How old is your house dean is? ')):
    return f"Faculty of {self.house_name} dean ({self.dean}) is {age} years old"
    
  def __str__(self):
    return f"This is house of {self.house_name}, {self.dean} is the house dean"


# parent class
class faculty:
  def __init__(self, faculty_name, dean):
    self.faculty_name = faculty_name
    self.dean = dean
    
  def faculty_info(self, age=input('How old is your faculty dean is? ')):
    return f"Faculty of {self.faculty_name} dean ({self.dean}) is {age} years old"
    
  def __str__(self):
    return f"This is faculty of {self.faculty_name}, {self.dean} is the faculty dean"
  
  
  
# a class that inherit from Faculty
class department(faculty):
  def __init__(self, faculty_name, dean, dept_name, H_O_D):
    super().__init__(faculty_name, dean)
    self.dept_name = dept_name
    self.H_O_D = H_O_D
    
  def department_info(self, age=input('How old is your department h.o.d is? ')):
    return f"Department of {self.dept_name} h.o.d ({self.H_O_D}) is {age} years old"
    
  def __str__(self):
    return f"Thsi is department of {self.dept_name}, {self.H_O_D} is the department H.O.D"
  
  
  
# a class that inherit from department
class student(department, faculty, house):
  def __init__(self, faculty_name, dean, dept_name, H_O_D, student_name, level, year):
    super().__init__(faculty_name, dean, dept_name, H_O_D)
    """
      the below two super are used to call multiple super class, equivalent to
      `department.__init__(self) and faculty.__init__(self)`
    """
    super(department, self).__init__(faculty_name, dean) # for faculty 
    super(faculty, self).__init__(faculty_name, dean) # for house
    
    # super(department, self).__init__(*args, **Kwargs)
    
    self.student_name = student_name
    self.level = level
    self.year = year
    
    
  def student_info(self, age=input('How old are you student? ')):
    return f"Student of faculty of {self.faculty_name}, department of {self.dept_name} ({self.student_name}) is {age} years old"
    
    
  def __str__(self):
    return f"This is student of faculty of {self.faculty_name} department of {self.dept_name}, {self.student_name} is {self.level} level student in the year {self.year}"
  
  
# print()
# f = faculty('science', 'Sani Salim')
# print(f)
# print(f.faculty_info())


# print()
# d = department('science', 'Sani Salim', 'physics', 'Ahmad Nura')
# print(d)
# print(d.department_info())


print()
s = student('science', 'Sani Salim', 'physics', 'Ahmad Nura', 'Usman Musa', 200, 2022)
print(s)
print(s.faculty_info())
print(s.department_info())
print(s.student_info())
