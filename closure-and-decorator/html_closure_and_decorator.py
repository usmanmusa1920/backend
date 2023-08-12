
# function base decorator: https://stackoverflow.com/questions/739654/how-do-i-make-function-decorators-and-chain-them-together

# class base decorator: https://stackoverflow.com/questions/5929107/decorators-with-parameters/5929178#5929178


"""   Closure   """
# A closure is the combination of a function bundled together (enclosed) with references to its
# surrounding state (the lexical environment). In other words, a closure gives you access to an outer
# function's scope from an inner function.

"""   Dcorator and closure   """
# A decorator is a function that takes in a function and returns an augmented copy of that function.
# When writing closures and decorators, you must keep the scope of each function in mind. In Python,
# functions define scope. Closures have access to the scope of the function that returns them;
# the decorator's scope.


"""   Closure code   """
def outer():
    x = 10
    def inner():
        y = 20
        return y
    y = inner()
    return "The result is %i" % eval(f"{x + y}")

my_func = outer
# print(my_func())
# Output:
#   The result is 30

def html_tag(tag):
    def print_tag(text):
        return '<{0}>{1}</{0}>'.format(tag, text)
    return print_tag

h1_tag = html_tag('h1')
# print(h1_tag) # this will print ``` <function html_tag.<locals>.print_tag at 0x7f9c808879d0> ```
# print(h1_tag('This is a h1 tag of html (headline!)'))
# Output:
#   <h1>This is a h1 tag of html (headline!)</h1>


"""   Decorators code   """
from functools import wraps
import time

def my_timer(orig_func):
    # @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Usman', 19)
# Output:
#   display_info ran with arguments (Usman, 19) # this is, the function output
#   display_info ran in: 1.0009398460388184 sec # this is, the decorator output


def c_alpha(v):
    return 1 if v == 5 else 2 # this is a one line if else statement
# print(c_alpha(5)) # output: 1
# print(c_alpha(3)) # output: 2
