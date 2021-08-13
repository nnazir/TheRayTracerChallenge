# Chapter 3 - Putting It Together
from trtc import Matrix, Tuple

#1
a = Matrix.identity_matrix()
b = a.inverse()
assert a == b

#2
a = Matrix([[3, -9, 7, 3], [3, -8, 2, -9], [-4, 4, 4, 1], [-6, 5, -1, 1]])
b = a * b.inverse()
print(b.matrix)
assert a == b

#3
print(a.matrix)
b = a.transpose().inverse()
c = a.inverse().transpose()
print(b.matrix)
print(c.matrix)
assert b == c

#4
id = Matrix.identity_matrix()
id.matrix[0][0] = 2
t = Tuple(1, 2, 3, 1)
a = id * t
print(id.matrix)
print(a)