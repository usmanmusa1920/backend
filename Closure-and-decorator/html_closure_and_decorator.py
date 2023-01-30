
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

print(h1_tag) # this will print ``` <function html_tag.<locals>.print_tag at 0x7f9c808879d0> ```
print(h1_tag('This is a h1 tag of html (headline!)'))
# Output:
#   <h1>This is a h1 tag of html (headline!)</h1>


"""   Decorator code   """
# # Decorators
# from functools import wraps


# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)

#     return wrapper


# def my_timer(orig_func):
#     import time

#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(orig_func.__name__, t2))
#         return result

#     return wrapper

# import time


# @my_logger
# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info('Tom', 22)

from functools import wraps
import time
def my_timer(orig_func):
    import time

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
# display_info('Tom', 22)



def c_alpha(v):
    return 1 if v == 5 else 2
# print(c_alpha(5))
# print(c_alpha(3))
