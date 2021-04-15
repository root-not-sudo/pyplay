import numpy as np
a = np.array([1, 2, 3])
b = a
c = [1, 2, 3]
d = 0
e = 5


for i in range(5):
    print('d =', d, 'it\'s address is: ', hex(id(d)))
    d = d+1

print(hex(id(d)))
print(d)
print(hex(id(e)))
print(e)
print('a is b:', a is b)
print('a == b:', a == b)
print('a is c:', a is c)
print('a == c:', a == c)
print('b is c:', b is c)
print('b == c:', b == c)
print('d is e:', d is e)
print('d == e:', d is e)

x = 'Earth is a planet'
y = 'Earth is a planet'
y = 30
y = "Earth is a planet"
z = 5
w = 5.0
p = 5 / 1
print(x == y)
print(x is y)
print(z == w)
print(z is w)
print(p == w)
print(p is w)
print(hex(id(x)))
print(hex(id(y)))
print(hex(id(z)))
print(hex(id(w)))
print(hex(id(p)))
