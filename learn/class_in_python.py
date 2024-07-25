# parent class
class Faculty:
    def __init__(self, faculty_name, dean):
        self.faculty_name = faculty_name
        self.dean = dean
        
    def faculty_info(self, age=input('How old is your faculty dean is? ')):
        return f"Faculty of {self.faculty_name} dean ({self.dean}) is {age} years old"
        
    def __str__(self):
        return f"This is faculty of {self.faculty_name}, {self.dean} is the faculty dean"
    

# a class that inherit from Faculty
class Department(Faculty):
    def __init__(self, faculty_name, dean, dept_name, H_O_D):
        super().__init__(faculty_name, dean)
        self.dept_name = dept_name
        self.H_O_D = H_O_D
        
    def department_info(self, age=input('How old is your department h.o.d is? ')):
        return f"Department of {self.dept_name} h.o.d ({self.H_O_D}) is {age} years old"
        
    def __str__(self):
        return f"Thsi is department of {self.dept_name}, {self.H_O_D} is the department H.O.D"
    

# a class that inherit from department
class Student(Department):
    def __init__(self, faculty_name, dean, dept_name, H_O_D, student_name, level, year):
        super().__init__(faculty_name, dean, dept_name, H_O_D)
        self.student_name = student_name
        self.level = level
        self.year = year
        
    def student_info(self, age=input('How old are you student? ')):
        return f"Student of faculty of {self.faculty_name}, department of {self.dept_name} ({self.student_name}) is {age} years old"
        
    def __str__(self):
        return f"This is student of faculty of {self.faculty_name} department of {self.dept_name}, {self.student_name} is {self.level} level student in the year {self.year}"
    

"""For calling the faculty class"""
# print()
# f = Faculty('science', 'Sani Salim')
# print(f)
# print(f.faculty_info())


"""For calling the department class"""
# print()
# d = Department('science', 'Sani Salim', 'physics', 'Ahmad Nura')
# print(d)
# print(d.department_info())


"""For calling the student class"""
print()
s = Student('science', 'Sani Salim', 'physics', 'Ahmad Nura', 'Usman Musa', 200, 2022)
print(s)
print(s.faculty_info())
print(s.department_info())
print(s.student_info())
