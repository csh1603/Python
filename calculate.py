'''
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) # 2^3 = 8
print(5%3)
print(5//3) #1

print(10 > 3)
print(4 >= 7)


print(1 != 2)
print(not(1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))

print(5 > 4 > 3)
print(5 > 4 > 7)


print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4 #14
print(number)
number = number + 2 #16
print(number)
number += 2 #18
print(number)
number *= 2 #36
print(number)
number /= 2 #18
print(number)
number -= 2 #16
print(number)

number %= 5 #1
print(number)

print(abs(-5)) # 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5
'''

from math import *
print(floor(4.99)) # 내림 -> 4
print(ceil(3.14)) # 올림 -> 4
print(sqrt(16)) # 제곱근 -> 4
