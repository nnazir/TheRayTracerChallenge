from trtc import Matrix, point, vector


def test_multiply_by_translation_matrix():
    """
    Scenario: Multiplying by a translation matrix
    """
    transform = Matrix.translation(5, -3, 2)
    p = point(-3, 4, 5)
    assert transform * p == point(2, 1, 7)


def test_multiply_by_inverse_translation_matrix():
    """
    Scenario: Multiplying by the inverse of a translation matrix
    """
    transform = Matrix.translation(5, -3, 2)
    inv = transform.inverse()
    p = point(-3, 4, 5)
    assert inv * p == point(-8, 7, 3)


def test_translate_vectors():
    """
    Scenario: Translation does not affect vectors
    """
    transform = Matrix.translation(5, -3, 2)
    v = vector(-3, 4, 5)
    assert transform * v == v
