import pytest
import math
from trtc import Tuple, point, vector


def test_point():
    '''
    Scenario: point() creates tupes with w=1
    '''
    p = point(4, -4, 3)
    assert p == Tuple(4, -4, 3, 1)


def test_vector():
    '''
    Scenario: vector() creates tuples with w=0
    '''
    v = vector(4, -4, 3)
    assert v == Tuple(4, -4, 3, 0)


def test_add_two_tuples():
    '''
    Scenario: Adding two tuples
    '''
    a1 = Tuple(3, -2, 5, 1)
    a2 = Tuple(-2, 3, 1, 0)
    assert a1 + a2 == Tuple(1, 1, 6, 1)


def test_subtract_two_points():
    '''
    Scenario: Subtracting two points
    '''
    p1 = point(3, 2, 1)
    p2 = point(5, 6, 7)
    assert p1 - p2 == vector(-2, -4, -6)


def test_subtract_vector_from_point():
    '''
    Scenario: Subtracting a vector from a point
    '''
    p = point(3, 2, 1)
    v = vector(5, 6, 7)
    assert p - v == point(-2, -4, -6)


def test_subtract_two_vectors():
    '''
    Scenario: Subtracting two vectors
    '''
    v1 = vector(3, 2, 1)
    v2 = vector(5, 6, 7)
    assert v1 - v2 == vector(-2, -4, -6)


def test_subtract_vector_from_zero():
    '''
    Scenario: Subtracting a vector from the zero vector
    '''
    zero = vector(0, 0, 0)
    v = vector(1, -2, 3)
    assert zero - v == vector(-1, 2, -3)


def test_negate_tuple():
    '''
    Scenario: Negating a tuple
    '''
    a = Tuple(1, -2, 3, -4)
    assert -a == Tuple(-1, 2, -3, 4)


def test_multiply_tuple_by_scalar():
    '''
    Scenario: Multiplying a tuple by a scalar
    '''
    a = Tuple(1, -2, 3, -4)
    assert a * 3.5 == Tuple(3.5, -7, 10.5, -14)


def test_multiply_tuple_by_fraction():
    '''
    Scenario: Multiplying a tuple by a fraction
    '''
    a = Tuple(1, -2, 3, -4)
    assert a * 0.5 == Tuple(0.5, -1, 1.5, -2)


def test_divide_tuple_by_scalar():
    '''
    Dividing a tuple by a scalar
    '''
    a = Tuple(1, -2, 3, -4)
    assert a / 2 == Tuple(0.5, -1, 1.5, -2)


def test_compute_magnitude_of_vector_1_0_0():
    '''
    Scenario: Computing the magnitude of vector(1, 0, 0)
    '''
    v = vector(1, 0, 0)
    assert v.magnitude() == 1


def test_compute_magnitude_of_vector_0_1_0():
    '''
    Scenario: Computing the magnitude of vector(0, 1, 0)
    '''
    v = vector(0, 1, 0)
    assert v.magnitude() == 1


def test_compute_magnitude_of_vector_0_0_1():
    '''
    Scenario: Computing the magnitude of vector(0, 0, 1)
    '''
    v = vector(0, 0, 1)
    assert v.magnitude() == 1


def test_compute_magnitude_of_vector_1_2_3():
    '''
    Scenario: Computing the magnitude of vector(1, 2, 3)
    '''
    v = vector(1, 2, 3)
    assert v.magnitude() == math.sqrt(14)


def test_compute_magnitude_of_vector_negative_1_2_3():
    '''
    Scenario: Computing the magnitude of vector(-1, -2, -3)
    '''
    v = vector(-1, -2, -3)
    assert v.magnitude() == math.sqrt(14)


def test_normalize_vector_1():
    '''
    Scenario: Normalizing vector(4,0, 0) gives (1, 0, 0)
    '''
    v = vector(4, 0, 0)
    assert v.normalize() == vector(1, 0, 0)


def test_normalize_vector_2():
    '''
    Scenario: Normalizing vector(1, 2, 3)
    '''
    v = vector(1, 2, 3)
    assert v.normalize() == vector(0.26726, 0.53452, 0.80178)


def test_magnitude_of_normalized_vector():
    '''
    Scenario: The magnitude of a normalized vector
    '''
    v = vector(1, 2, 3)
    norm = v.normalize()
    assert norm.magnitude() == 1


def test_dot_product_of_two_tuples():
    '''
    Scenario: The dot product of two tuples
    '''
    a = vector(1, 2, 3)
    b = vector(2, 3, 4)
    assert a.dot(b) == 20


def test_cross_product_of_two_vectors():
    '''
    Scenario: The cross product of two vectors
    '''
    a = vector(1, 2, 3)
    b = vector(2, 3, 4)
    assert a.cross(b) == vector(-1, 2, -1)
    assert b.cross(a) == vector(1, -2, 1)



