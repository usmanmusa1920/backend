import subprocess

subprocess.run(['clear'])

cache_data = {}
def fibonacci(num):
    if num in cache_data:
        return cache_data[num]
    if num >= 3:
        value = fibonacci(num - 1) + fibonacci(num - 2)
    else:
        value = 1
    cache_data[num] = value
    return value
for i in range(1, 10):
    print('Fibonacci of', i, 'is', fibonacci(i))
    