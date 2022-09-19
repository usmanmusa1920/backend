#!/bin/usr/python3

def func(*args, **kwargs):
  """
  args: are used to accept unlimited positional argument to a function or class.
    the name `args` is the convention we can call it what ever we want,
    it usually start with single asteric `*args`
    
  kwargs: are used to accept unlimited key-word argument to a function or class.
    the name `kwargs` is the convention we can call it what ever we want,
    it usually start with double asteric `**kwargs`
  """
  
  print(*args)
  print(*kwargs)
  
  # print(type(*args))
  # print(type(*kwargs))
  
func('1', '2', '3', a='4', b='5', c='6')
