# A naive recursive solution
def fibonacci(num):
    if num >= 3:
        result = fibonacci(num - 1) + fibonacci(num - 2)
    else:
        result = 1
    return result
    
for i in range(1, 13):
    print('Fibonacci of', i, 'is', fibonacci(i))
    