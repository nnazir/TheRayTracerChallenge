from trtc.tuple import Tuple
import numpy as np
from trtc.utils import float_equal


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

    @staticmethod
    def identity_matrix():
        return Matrix([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

    def transpose(self):
        return Matrix([
            [self.matrix[0][0], self.matrix[1][0], self.matrix[2][0], self.matrix[3][0]],
            [self.matrix[0][1], self.matrix[1][1], self.matrix[2][1], self.matrix[3][1]],
            [self.matrix[0][2], self.matrix[1][2], self.matrix[2][2], self.matrix[3][2]],
            [self.matrix[0][3], self.matrix[1][3], self.matrix[2][3], self.matrix[3][3]],
            ]
        )
