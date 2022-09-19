"""
  IF STATEMENT
  If statement in python (condition) is a way to make a condition if something then do something, and it is used along with the python 'if, elif, and else' keywords. e.g:
    a =  10
    b = 15
    if a > b:
      print(a, 'is greater than', b)
    elif a < b:
      print(a, 'is less than', b)
    else:
      print(a, 'is equal to', b)
"""

"""
  FUNCTION
  Function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a  result. e.g
    def my_func():
      print('Hi, welcome to python function')
      
  To call the above function, use the function name and followed by parantheses, e.g
    myfunc()
    
  Function parameter are specified after the function name, inside the parantheses, you can add as many as want, whether a variable, list, set,  tuple, etc. e.g
    def my_func(full_name, age):
      print('I am', full_name, 'My age is', age)
      
    my_func('Usman Musa', 15)
    # output: I am Usman Musa My age is 15
    
  You can make a default value for a parameter, in such a way even if the parametter is not pass into the function, it will use the default one. But if you pass a value it will replace the default one to the one you pass into the function. e.g
    def my_func(full_name='Anonymous User', age=15):
      print('I am', full_name, 'My age is', age)
      
    my_func()
    # output: I am Anonymous User My age is 15
    
    my_func('Usman Musa', 12)
    # output: I am Usman Musa My age is 12
    
  To let your function to return a value, use the return keyword statement
    def my_func(full_name='Anonymous User'):
      return f'I am, {full_name}'
      
    print(my_func('Usman Musa'))
    # output: I am Usman Musa
  
"""
