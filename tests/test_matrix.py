from trtc import Matrix, Tuple, matrix
from trtc.utils import float_equal


def test_construct_4x4_matrix():
    """
    Scenario: Constructing and inspecting a 4x4 matrix
​ 	  ​Given​ the following 4x4 matrix M:
​ 	    |  1   |  2   |  3   |  4   |
​ 	    |  5.5 |  6.5 |  7.5 |  8.5 |
​ 	    |  9   | 10   | 11   | 12   |
​ 	    | 13.5 | 14.5 | 15.5 | 16.5 |
    """
    M = Matrix([[1, 2, 3, 4],
                [5.5, 6.5, 7.5, 8.5],
                [9, 10, 11, 12],
                [13.5, 14.5, 15.5, 16.5]])
    assert M.matrix[0][0] == 1
    assert M.matrix[0][3] == 4
    assert M.matrix[1][0] == 5.5
    assert M.matrix[1][2] == 7.5
    assert M.matrix[2][2] == 11
    assert M.matrix[3][0] == 13.5
    assert M.matrix[3][2] == 15.5


def test_2x2_matrix_is_representable():
    """
    Scenario: A 2x2 matric ought to be representable
    """
    M = Matrix([[-3, 5],
                [1, -2]])
    assert M.matrix[0][0] == -3
    assert M.matrix[0][1] == 5
    assert M.matrix[1][0] == 1
    assert M.matrix[1][1] == -2


def test_3x3_matrix_is_representable():
    """
    Scenario: A 3x3 matrix ought to be representable
    """
    M = Matrix([[-3, 5, 0],
               [1, -2, -7],
               [0, 1, 1]])
    assert M.matrix[0][0] == -3
    assert M.matrix[1][1] == -2
    assert M.matrix[2][2] == 1


def test_matrix_equality_identical_matrices():
    """
    Scenario: Matrix equality with identical matrices
    """
    A = Matrix([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 8, 7, 6],
                [5, 4, 3, 2]])
    B = Matrix([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 8, 7, 6],
                [5, 4, 3, 2]])
    assert A == B

    def test_matrix_equality_different_matrices():
        """
        Scenario: Matrix equality with different matrices
        """
    A = Matrix([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 8, 7, 6],
                [5, 4, 3, 2]])
    B = Matrix([[2, 3, 4, 5],
                [6, 7, 8, 9],
                [8, 7, 6, 5],
                [4, 3, 2, 1]])
    assert A != B


def test_multiply_two_matricies():
    """
    Scenario: Multiplying two matrices
    """
    A = Matrix([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 8, 7, 6],
                [5, 4, 3, 2]])
    B = Matrix([[-2, 1, 2, 3],
                [3, 2, 1, -1],
                [4, 3, 6, 5],
                [1, 2, 7, 8]])
    assert A * B == Matrix([[20, 22, 50, 48],
                            [44, 54, 114, 108],
                            [40, 58, 110, 102],
                            [16, 26, 46, 42]])


def test_matrix_multiplied_by_tuple():
    """
    Scenario: A matrix multiplied by a tuple
    """
    A = Matrix([[1, 2, 3, 4],
                [2, 4, 4, 2],
                [8, 6, 4, 1],
                [0, 0, 0, 1]])
    b = Tuple(1, 2, 3, 1)
    assert A * b == Tuple(18, 24, 33, 1)


def test_multiply_matrix_by_identity():
    """
    Scenario: Multiplying a matrix by the identity matrix
    """
    A = Matrix([[0, 1, 2, 4],
                [1, 2, 4, 8],
                [2, 4, 8, 16],
                [4, 8, 16, 32]])
    assert A * Matrix.identity_matrix() == A


def test_multiply_identity_matrix_by_tuple():
    """
    Scenario: Multiplying the identity matrix by a tuple
    """
    a = Tuple(1, 2, 3, 4)
    assert Matrix.identity_matrix() * a == a


def test_transpose_matrix():
    """
    Scenario: Transposing a matrix
    """
    A = Matrix([[0, 9, 3, 0],
                [9, 8, 0, 8],
                [1, 8, 5, 3],
                [0, 0, 5, 8]])
    assert A.transpose() == Matrix([[0, 9, 1, 0],
                                    [9, 8, 8, 0],
                                    [3, 0, 5, 5],
                                    [0, 8, 3, 8]])


def test_transpose_identity_matrix():
    """
    Scenario: Transposing the identity matrix
    """
    A = Matrix.identity_matrix()
    assert A.transpose() == Matrix.identity_matrix()


def test_calculate_determinant_2x2_matrix():
    """
    Scenario: Calculating the determinant of a 2x2 matrix
    """
    A = Matrix([[1, 5], [-3, 2]])
    assert A.determinant() == 17


def test_submatrix_of_3x3_matris():
    """
    Scenario: A submatrix of a 3x3 matrix is a 2x2 matrix
    """
    A = Matrix([[1, 5, 0],
                [-3, 2, 7],
                [0, 6, -3]])
    assert A.submatrix(0, 2) == Matrix([[-3, 2], [0, 6]])


def test_submatrix_of_4x4_matrix():
    """
    Scenario: A submatrix of a 4x4 matrix is a 3x3 matrix
    """
    A = Matrix([[-6, 1, 1, 6],
                [-8, 5, 8, 6],
                [-1, 0, 8, 2],
                [-7, 1, -1, 1]
                ])
    assert A.submatrix(2, 1) == Matrix([[-6, 1, 6], [-8, 8, 6], [-7, -1, 1]])


def test_minor_3x3_matrix():
    """
    Scenario: Calculating a minor of a 3x3 matrix
    """
    A = Matrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
    B = A.submatrix(1, 0)
    assert B.determinant() == 25
    assert A.minor(1, 0) == 25


def test_cofactor_3x3_matrix():
    """
    Scenario: Calculating a cofactor of a 3x3 matrix
    """
    A = Matrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
    assert A.minor(0, 0) == -12
    assert A.cofactor(0, 0) == -12
    assert A.minor(1, 0) == 25
    assert A.cofactor(1, 0) == -25


def test_determinant_3x3_matrix():
    """
    Scenario: Calculating the determinant of a 3x3 matrix
    """
    A = Matrix([[1, 2, 6], [-5, 8, -4], [2, 6, 4]])
    assert A.cofactor(0, 0) == 56
    assert A.cofactor(0, 1) == 12
    assert A.cofactor(0, 2) == -46
    assert A.determinant() == -196


def test_determinant_of_4x4_matrix():
    """
    Scenario: Calculating the determinant of a 4x4 matrix
    """
    A = Matrix([[-2, -8, 3, 5], [-3, 1, 7, 3], [1, 2, -9, 6], [-6, 7, 7, -9]])
    assert A.cofactor(0, 0) == 690
    assert A.cofactor(0, 1) == 447
    assert A.cofactor(0, 2) == 210
    assert A.cofactor(0, 3) == 51
    assert A.determinant() == -4071


def test_matrix_invertibility():
    """
    Scenario: Testing an invertible matrix for invertibility
    """
    A = Matrix([[6, 4, 4, 4], [5, 5, 7, 6], [4, -9, 3, -7], [9, 1, 7, -6]])
    assert A.determinant() == -2120
    assert A.is_invertible() == True


def test_noninvertible_matrix():
    """
    Scenario: Testing a noninvertible matrix for invertibility
    """
    A = Matrix([[-4, 2, -2, -3], [9, 6, 2, 6], [0, -5, 1, -5], [0, 0, 0, 0, ]])
    assert A.determinant() == 0
    assert A.is_invertible() == False


def test_calculate_matrix_inverse_1():
    """
    Scenario: Calculating the inverse of a matrix
    """
    A = Matrix([[-5, 2, 6, -8], [1, -5, 1, 8], [7, 7, -6, -7], [1, -3, 7, 4]])
    B = A.inverse()
    assert A.determinant() == 532
    assert A.cofactor(2, 3) == -160
    assert float_equal(B.matrix[3][2], -160/532)
    assert A.cofactor(3, 2) == 105
    assert float_equal(B.matrix[2][3], 105/532)
    assert B == Matrix([[0.21805, 0.45113, 0.24060, -0.04511],
                        [-0.80827, -1.45677, -0.44361,  0.52068],
                        [-0.07895, -0.22368, -0.05263,  0.19737],
                        [-0.52256, -0.81391, -0.30075,  0.30639],
                        ])


def test_calculate_matrix_inverse_2():
    """
    Scenario: Calculating the inverse of another matrix
    """
    A = Matrix([[8, -5, 9, 2], [7, 5, 6, 1], [-6, 0, 9, 6], [-3, 0, -9, -4]])
    assert A.inverse() == Matrix(
        [[-0.15385, -0.15385, -0.28205, -0.53846],
         [-0.07692,  0.12308,  0.02564,  0.03077],
         [0.35897,  0.35897,  0.43590,  0.92308],
         [-0.69231, -0.69231, -0.76923, -1.92308]])


def test_calculate_matrix_inverse_3():
    """
    Scenario: Calculating the inverse of a third matrix
    """
    A = Matrix([
        [9, 3, 0, 9],
        [-5, -2, -6, -3],
        [-4, 9, 6, 4],
        [-7, 6, 6, 2]
    ])
    assert A.inverse() == Matrix([
        [-0.04074, -0.07778, 0.14444, -0.22222],
        [-0.07778, 0.03333, 0.36667, -0.33333],
        [-0.02901, -0.14630, -0.10926, 0.12963],
        [0.17778, 0.06667, -0.26667, 0.33333]
    ])
