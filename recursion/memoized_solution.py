# Memoized solution
def fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib(n, memo)

print(fib_memo(8))
