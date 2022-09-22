from functools import lru_cache

# By default python lru_cache will cache 128. But in the case of you want to deal with many number recursively, you have to indicate a maxsize lru_cache that will suit your recursive call function.  --- OR ---   Set maxsize to None if you want no bound i.e no limit

@lru_cache(maxsize = None)
def fib(indx):

    if indx == 1 or indx == 2:
        return 1

    else:
        return fib(indx - 1) + fib(indx - 2)

for i in range(1, 101):
    print('Fibonacci sequence of', i, 'is', fib(i))
    