# JUST like a __init__ in a class which runs automatically as soon as the class instanciated,
# the __init__.py file runs automatically as soon as a library is imported.
# E.g as we say 'import f1' it look and runs the __init__.py file


import req
import f1


o = f1.one()
u = f1.two()
class A:
  def __init__(self, *args, **kwargs):
    print('init')
    
    
# print(type(A.__new__(2, x=1)).init(4, X=1))

# print(dir(req))
# r = req.get('http://127.0.0.1:8000')
# print(r.text)
