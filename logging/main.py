import logging

"""
  NOTSET    ---  0
  DEBUG     ---  10
  INFO      ---  20
  WARNING   ---  30  (default)
  ERROR     ---  40
  CRITICAL  ---  50
"""

import second
# logging.info(second.s1)
# logging.info(second.s2)
# logging.info(second.s3)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#when we did not use the logger variable in the basicConfig class (for kwargs, e.g logger.INFO instead logging.INFO) it will use the default one because it is in heirachey

formatter = logging.Formatter(' [+] %(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('main.log')

#to let logging to only login error statement (only if error)
#file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)

#to print logs on console
stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

#logging.basicConfig(filename='main.log', level=logging.DEBUG, format=' [+] %(asctime)s:%(levelname)s:%(message)s')


def add(a, b):
  """ an addition function """
  r = a + b
  return f"The addition of {a} and {b} is: {r}"


def subt(a, b):
  """ a subtraction function """
  r = a - b
  return f"The subtraction of {a} and {b} is: {r}"


def mult(a, b):
  """ a multiplication function """
  r = a * b
  return f"The multiple of {a} and {b} is: {r}"


def div(a, b):
  """ a division function """
  try:
    r = a / b
  except ZeroDivisionError:
    #to include the traceback of the error
    logger.exception('Try to divide by zero')
  else:
    return f"the division of {a} by {b} is: {r}"

def info():
  """ an informaion function """
  return f'Hi i am from main'

num1 = 8
num2 = 0
# num1 = 20
# num2 = 10

logger.debug(add(num1, num2))
logger.debug(subt(num1, num2))
logger.debug(mult(num1, num2))
logger.debug(div(num1, num2))













