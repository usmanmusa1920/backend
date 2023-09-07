print('Method one 1A')
num = int(input('Enter a number: '))
num=10
list1 = []

for i in range(num):
        list1.append([])
        list1[i].append(1)
        for j in range(1, i):
                list1[i].append(list1[i-1][j-1]+list1[i-1][j])
        if(num!=0):
                list1[i].append(1)
print('\nMethod one 1B')


for i in range(num):
        print(' ' * (num-i),end='',sep='')
        for j in range(0,i+1):
                print('{0:6}'.format(list1[i][j]),end='',sep='')
        print()
        
        
for i in range(6):
        print(11**i)
print('\nMethod two 2')


n = int(input('Enter the number of rows:'))
for i in range(1,n+1):
        for j in range(0,n-i+1):
                print(' ',end='')
        c=1
        for j in range(1,i+1):
                print(' ',c,sep='',end='')
                cc=c*(i-j)//j
        print()
print('\nMethod three 3')
n = 13


for i in range(1,n):
        print(' '*(n-i),end='')
        print(' '.join(map(str, str(11**i))))


