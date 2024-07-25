import time
import sys


def f(num):
    for i in num:
        print('\tThe loop is on', i)
        time.sleep(1)
    
    
for l in sys.stdin:
    # if 'q' == l.rstripe():
    #     break
    print(f'Input: {l}')

print('Exit')


if __name__ == "__main__":
    f(sys.argv[1])
