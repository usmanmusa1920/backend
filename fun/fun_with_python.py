import time
import subprocess

# clearing the screen
subprocess.run(['clear'])

# maths tables
def tables(star,num,n=False):
    if not n:
        n = 3
        
    tab = ['Addition', 'Subtraction', 'Multiplication', 'Division']
    b_top = '\t' + '-' * star
    
    o = 0.3
    
    # Addition
    print('\n'*n+'\t' + tab[0] + ' table:\n' + b_top)
    for i in range(1, num):
        time.sleep(o)
        print('\t|\t\t' + str(i) + ' + 2 = ' + str(i + 2) + '\t\t    |')

    # Subtraction
    print(b_top + '\n'*n+'\t' + tab[1] + ' table:\n' + b_top)
    for i in range(1, num):
        time.sleep(o)
        print('\t|\t\t20 - ' + str(i) + ' = ' + str(20 - (i)) + '\t\t    |')

    # Multiplication
    print(b_top + '\n'*n+'\t' + tab[2] + ' table:\n' + b_top)
    for i in range(1, num):
        time.sleep(o)
        print('\t|\t\t5 * ' + str(i) + ' = ' + str(5 * i) + '\t\t    |')

    # Division
    print(b_top + '\n'*n+'\t' + tab[3] + ' table:\n' + b_top)
    for i in range(1, num):
        time.sleep(o)
        print('\t|\t\t40 / ' + str(i) + ' = ' + str('%.2f'%float(40 / i)) + '\t\t    |')

    print(b_top + '\n' * n)
    lst = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in lst:
        k = '\t'.join(i)
        time.sleep(0.5)

        # here the script will try to see if there is banner installed in the machine
        try:
            subprocess.run(['banner', k])
        except:
            pass


tables(45,13,2)
time.sleep(2)

print('\t\tThis car is for sale \n\n\t\t      ' + '-' * 10)
time.sleep(1)
print('\t\t     /' + ' ' * 10 + '\\\n\t\t    /' + ' ' * 12 + '\\\n\t\t ---' + ' ' * 14 + '\\----\n\t\t |' + ' ' * 16 + '    |')

print('\t\t -----O--------O------- \n\n')
time.sleep(2)
print('\t  O\n\t  |\n\t /|\\   Usman is selling this kind of cars at his deport:\n\t  |\n\t / \\\twww.github.com/usmanmusa1920\n\n')


time.sleep(2)
try:
    subprocess.run(['banner', ' Program'])
    subprocess.run(['banner', ' Finished!'])
except:
    print('Program finished')
