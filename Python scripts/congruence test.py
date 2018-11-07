#Tests if numbers are congruent to each other
print('Test if b is congruent to c modulus m.')
b = int(input('What is b: '))
c = int(input('What is c: '))
m = int(input('What is m: '))
ans = (b-c)/m
if ans.is_integer():
    print('{} is congruent to {}(modulus {})'.format(b, c, m))
else:
    print('{} is not congruent to {}(modulus {})'.format(b, c, m))
input('Press enter to end: ')
"""
if b%c == m:
    pass
else:
    pass
"""
