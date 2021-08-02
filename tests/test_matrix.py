from trtc import Matrix, Tuple


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
