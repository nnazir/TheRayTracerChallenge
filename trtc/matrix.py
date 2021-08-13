from trtc.tuple import Tuple
from trtc.utils import float_equal
import numpy as np
import copy


class Matrix():
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def __eq__(self, o: object) -> bool:
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                if not float_equal(self.matrix[row][col], o.matrix[row][col]):
                    return False
        return True

    def __mul__(self, o):
        if type(o) is Matrix:
            return Matrix(np.matmul(self.list(), o.list()))
        else:
            return Tuple(np.dot(self.list()[0], o.list()),
                         np.dot(self.list()[1], o.list()),
                         np.dot(self.list()[2], o.list()),
                         np.dot(self.list()[3], o.list()))

    def list(self):
        return self.matrix

    def size(self):
        return len(self.matrix)

    @staticmethod
    def identity_matrix():
        return Matrix([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

    def transpose(self):
        return Matrix([
            [self.matrix[0][0], self.matrix[1][0],
                self.matrix[2][0], self.matrix[3][0]],
            [self.matrix[0][1], self.matrix[1][1],
                self.matrix[2][1], self.matrix[3][1]],
            [self.matrix[0][2], self.matrix[1][2],
                self.matrix[2][2], self.matrix[3][2]],
            [self.matrix[0][3], self.matrix[1][3],
                self.matrix[2][3], self.matrix[3][3]],
        ]
        )

    def determinant(self):
        if self.size() == 2:
            det = self.matrix[0][0] * self.matrix[1][1] - \
                self.matrix[0][1] * self.matrix[1][0]
        else:
            det = 0
            for column in range(self.size()):
                det = det + self.matrix[0][column] * self.cofactor(0, column)
        return det

    def submatrix(self, row, column):
        m = copy.deepcopy(self.matrix)
        del m[row]
        for i in m:
            del i[column]
        return Matrix(m)

    def minor(self, row, column):
        # return self.submatrix(row, column).determinant()
        t = self.submatrix(row, column)
        return t.determinant()

    def cofactor(self, row, column):
        if ((row + column) % 2 != 0):
            return -self.minor(row, column)
        return self.minor(row, column)

    def is_invertible(self):
        if self.determinant() == 0:
            return False
        return True

    def inverse(self):
        if not self.is_invertible():
            return None
        m2 = Matrix([[0 for i in range(self.size())]
                     for j in range(self.size())])
        det = self.determinant()
        for row in range(self.size()):
            for column in range(self.size()):
                m2.matrix[column][row] = self.cofactor(row, column)/det
        return m2

    @classmethod
    def translation(cls, x,y,z):
        m = Matrix.identity_matrix()
        m.matrix[0][3] = x
        m.matrix[1][3] = y
        m.matrix[2][3] = z
        return(m)
