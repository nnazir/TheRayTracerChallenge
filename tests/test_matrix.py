from trtc import Matrix


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
