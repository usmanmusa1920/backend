import time
#import mem_profile

#print(f'My memory before: {mem_profile.memory_usage_resource()}')
nums = [1,2,3,4,5,6]

def s_num(n):
  r = []
  for i in n:
    r.append(i*i)
  return r
 
t1 = time.time() 
my_num = s_num(nums)
t2 = time.time()



print(my_num)
print(f"Finish in {t2 - t1}")

#Generator
#generator don't hold all result in memory, it yield one result at a time
def _num(n):
  for i in n:
    yield (i*i)
 
t1 = time.time() 
my_num = _num(nums)
t2 = time.time()

print()
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print()

#instead of printing each result using next function, we can use forloop down below,
#because iteration will no exactly when to stop:
for i in _num(my_num):
  print(i)
  
print(f"Finish in {t2 - t1}")


#wec can use generator using list comprehension
my_nums = [i*i for i in nums]
for n in my_nums:
  print(f'We have {n}')

#it can also be create using:
gen = (i*i for i in nums)
print(f'My gen is:', gen)


#print(f'My memory after: {mem_profile.memory_usage_resource()}')













