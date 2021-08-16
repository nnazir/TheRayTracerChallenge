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


def test_rotate_point_around_y_axis():
    """
    Scenario: Rotating a point around the y axis
    """
    p = point(0, 0, 1)
    half_quarter = Matrix.rotation_y(math.pi / 4)
    full_quarter = Matrix.rotation_y(math.pi / 2)
    assert half_quarter * p == point(math.sqrt(2)/2, 0, math.sqrt(2)/2)
    assert full_quarter * p == point(1, 0, 0)


def test_rotate_point_around_z_axis():
    """
    Scenario: Rotating a point around the z axis
    """
    p = point(0, 1, 0)
    half_quarter = Matrix.rotation_z(math.pi / 4)
    full_quarter = Matrix.rotation_z(math.pi / 2)
    assert half_quarter * p == point(-math.sqrt(2)/2, math.sqrt(2)/2, 0)
    assert full_quarter * p == point(-1, 0, 0)


def test_shearing_x_to_y():
    """
    Scenario: A shearing transformation moves x in proportion to y
    """
    transform = Matrix.shearing(1, 0, 0, 0, 0, 0)
    p = point(2, 3, 4)
    assert transform * p == point(5, 3, 4)


def test_shearing_x_to_z():
    """
    Scenario: A shearing transformation moves x in proportion to z
    """
    transform = Matrix.shearing(0, 1, 0, 0, 0, 0)
    p = point(2, 3, 4)
    assert transform * p == point(6, 3, 4)


def test_shearing_y_to_x():
    """
    Scenario: A shearing transformation moves y in proportion to x
    """
    transform = Matrix.shearing(0, 0, 1, 0, 0, 0)
    p = point(2, 3, 4)
    assert transform * p == point(2, 5, 4)


def test_shearing_y_to_z():
    """
    Scenario: A shearing transformation moves y in proportion to z
    """
    transform = Matrix.shearing(0, 0, 0, 1, 0, 0)
    p = point(2, 3, 4)
    assert transform * p == point(2, 7, 4)


def test_shearing_z_to_x():
    """
    Scenario: A shearing transformation moves z in proportion to x
    """
    transform = Matrix.shearing(0, 0, 0, 0, 1, 0)
    p = point(2, 3, 4)
    assert transform * p == point(2, 3, 6)


def test_shearing_z_to_y():
    """
    Scenario: A shearing transformation moves x in proportion to y
    """
    transform = Matrix.shearing(0, 0, 0, 0, 0, 1)
    p = point(2, 3, 4)
    assert transform * p == point(2, 3, 7)


def test_individual_transformations():
    """
    Scenario: Individual transformations are applied in sequence
    """
    p = point(1, 0, 1)
    A = Matrix.rotation_x(math.pi / 2)
    B = Matrix.scaling(5, 5, 5)
    C = Matrix.translation(10, 5, 7)
    # apply rotation first
    p2 = A * p
    assert p2 == point(1, -1, 0)
    # then apply scaling
    p3 = B * p2
    assert p3 == point(5, -5, 0)
    # then apply translation
    p4 = C * p3
    assert p4 == point(15, 0, 7)


def test_chained_transformations():
    """
    Scenario: Chained transformations must be applied in reverse order
    """
    p = point(1, 0, 1)
    A = Matrix.rotation_x(math.pi / 2)
    B = Matrix.scaling(5, 5, 5)
    C = Matrix.translation(10, 5, 7)
    T = C * B * A
    assert T * p == point(15, 0, 7)
