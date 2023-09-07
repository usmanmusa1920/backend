# a program that will give us a factorial of a number

def factorial(num):
    if num >= 1:
        return num * factorial(num - 1)
    else:
        return 1
        
for i in range(1, 11):
    print('Factorial of', i, 'is', factorial(i))

