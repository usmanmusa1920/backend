x = 10

y = 2

x += y
print('The increment is', x)

x -= y
print('The decrement is', x)

x *= y
print('The multiple-increment is', x)

x /= y
print('The division increment is', x)

x **= y
print('The exponential increment is', x)

x //= y
print('The floor_division-increment is', x)

x %= y
print('The modulus-increment is', x)


# bitwise for binary
# basically binary are on base 2, that means,
# we look for numbers that are in power of two


# AND gate --- &
# OR gate --- |
# XOR gate --- ^
# NOT gate --- ~
# SHIFTS-LEFT --- <<=
#     this shift the zero to the left, e.g:
#           20 <<= 1 = 40 # i.e it multiply it by 2
#           40 <<= 1 = 80 # i.e it multiply it by 2

# SHIFTS-RIGHT --- >>=
#     this shift the zero to the right, e.g:
#           20 >>= 2 = 10 # i.e it divide it by 2
#           40 >>= 2 = 20 # i.e it divide it by 2



a = 28
print(bin(a)[2:])
# 16 + 8 + 4   ==  11100
#   this means:
#         yes for 16 (1)
#         yes for 8  (1)
#         yes for 4  (1)
#         no  for 2  (0)
#         no  for 1  (0)


b = 19
print(bin(b)[2:])
# 16 + 2 + 1   ==  10011
#   this means:
#         yes for 16 (1)
#         no  for 8  (0)
#         no  for 4  (0)
#         yes for 2  (1)
#         yes for 1  (1)

# read, write, execute, and edit
p1 = 0b0001
p2 = 0b0110
p3 = 0b0000
p4 = 0b1111

# all have to be true
p_true_all = p1 & p2 & p3 & p4

# not all have to be true
p_true_all = p1 | p2 | p3 | p4


# checking binary number to see if it is even or odd, using binary operator
someone = 3472348
# 1010111010101
# 0000000000001
if someone & 1 == 0:
    print('even')
else:
    print('odd')
