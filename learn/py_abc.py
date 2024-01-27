import abc

class AbstractClass1(metaclass=abc.ABCMeta):
	def abstractfunc(self):
		return None

print(AbstractClass1.register(dict))
# <class 'dict'>


class AbstractClass2(metaclass=abc.ABCMeta):
	def abstractfunc(self):
		return None

AbstractClass2.register(dict)
print(issubclass(dict, AbstractClass2))
# True


class MySequence(metaclass=abc.ABCMeta):
	pass

MySequence.register(list)
MySequence.register(tuple)

a = [1, 2, 3]
b = ('x', 'y', 'z')

print('List instance:', isinstance(a, MySequence))
print('Tuple instance:', isinstance(b, MySequence))
print('Object instance:', isinstance(object(), MySequence))
# List instance: True
# Tuple instance: True
# Object instance: False
