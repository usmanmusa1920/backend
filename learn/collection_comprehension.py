# list comprehension
print('for list:')
l = [i for i in range(1, 11)]
print(l)

# normal list for loop
for i in range(1,13):
  lst_comphnsn = [i for i in range(13)]
  print(lst_comphnsn[i], '* 2 = ', lst_comphnsn[i]*2)


# dictionary comprehension
print('for dictionary')
d = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
d = {k:v for k, v in d.items()}
print(d)

# normal dictionary for loop
d = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
for k, v in d.items():
  print(k, ':', v)
print()


# set comprehension
print('for set')
s = {i for i in {2, 'x', 'y', 5, 7}}
print(s)

# normal set for loop
for i in {2, 'x', 'y', 5, 7}:
  print(i)
print()
