data = [
    ['year', 'last', 'first'], 
    [1943, 'Idle', 'Eric'], 
    [1939, 'Cleese', 'John'] 
]


# here we do a for loop in the list of list above, and get the entire data for each list by the asteric sign
for row in data:
    print(*row, sep=', ', end=', ')
print()


S = 'Computer_of_computer'
d = {}

# here we count the number of alphabet in the string above (S), by nagating the duplicate but including how many times an alphabet appear
for i in S:
    d[i] = d.get(i, 0) + 1
print(d)
