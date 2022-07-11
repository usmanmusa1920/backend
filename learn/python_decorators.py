def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result
    
    
print(operate(inc,3))

@operate
def inc(x):
    return x + 1
print(inc(8),7)
