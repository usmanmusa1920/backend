def average(*args):
    # this function will give us the average of the number
    # we passed into the functions as an argument
    l = 0
    for i in args:
        l = l + i
    n = l / len(args)
    print('The average number of ', args, 'is "' + str(int(n)) + '"')
    print()
    
    
def time_to_second(minute = input('Input minute: ')):
    # converting miuntes into seconds
    mul = int(minute) * 60
    print(str(minute) + ' minutes in seconds is ' + str(mul) + ' seconds!')
    print()
    
    
    
def ask(a = input('Put number ')):
    # detecting number if less than ten, it will ask again,
    # else it will print the number and say it's OK'
    while int(a) <= 10:
        a = input(str(a) + ' is not allowed, try again: ')
        print()
    print('Ok,', str(a), 'is well now!')
    print()
    
    
    
print()
average(1,2,3,4,5)
time_to_second(minute = 36)
ask(a = 6)

