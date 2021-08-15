from trtc import Matrix, point, vector
import math


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


def test_scaling_matrix_applied_to_point():
    """
    Scenario: A scaling matrix applied to a point
    """
    transform = Matrix.scaling(2, 3, 4)
    p = point(-4, 6, 8)
    assert transform * p == point(-8, 18, 32)


def test_scaling_matrix_applied_to_vector():
    """
    Scenario: A scaling matrix applied to a vector
    """
    transform = Matrix.scaling(2, 3, 4)
    v = vector(-4, 6, 8)
    assert transform * v == vector(-8, 18, 32)


def test_multiply_by_inverse_of_scaling_matrix():
    """
    Scenario: Multiplying by the inverse of a scaling matrix
    """
    transform = Matrix.scaling(2, 3, 4)
    inv = transform.inverse()
    v = vector(-4, 6, 8)
    assert inv * v == vector(-2, 2, 2)


def test_reflect_scaling_negative_value():
    """
    Scenario: Reflection is scaling by a negative value
    """
    transform = Matrix.scaling(-1, 1, 1)
    p = point(2, 3, 4)
    assert transform * p == point(-2, 3, 4)


def test_rotate_point_around_x_axis():
    """
    Scenario: Rotating a point around the x axis
    """
    p = point(0, 1, 0)
    half_quarter = Matrix.rotation_x(math.pi / 4)
    full_quarter = Matrix.rotation_x(math.pi / 2)
    assert half_quarter * \
        p == point(0, math.sqrt(2)/2, math.sqrt(2)/2)
    assert full_quarter * p == point(0, 0, 1)


def test_inverse_x_rotation_rotates_opposite():
    """
    Scenario: The inverse of an x-rotation rotates in the opposite direction
    """
    p = point(0, 1, 0)
    half_quarter = Matrix.rotation_x(math.pi / 4)
    inv = half_quarter.inverse()
    assert inv * p == point(0, math.sqrt(2)/2, -math.sqrt(2)/2)
