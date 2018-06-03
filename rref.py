import sympy as sp


a = sp.Matrix([[1, -1, 2, 3], [3, 4, 2, 7], [0, 2, 2, 6]])
print(a.rref())
