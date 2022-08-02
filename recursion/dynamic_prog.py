# import subprocess
# subprocess.run(['clear'])

def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


for n in range(1,15):
    print(fib(n))
    
    
def fib_bot(n):
    if n == 1 or n == 2:
        return 1
    bot = [None] * (n + 1)
    bot[1] = 1
    bot[2] = 2
    # print('The fib of', str(idx + 1), bot[i])
    for idx, i in enumerate(range(3, n+1)):
        bot[i] = bot[i - 1] + bot[i - 2]
        print('The fib of', str(idx + 1), bot[i])
    return bot[n]
fib_bot(8)
