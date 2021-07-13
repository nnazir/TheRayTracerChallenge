import pytest
import tuple
import math


def test_point():
    '''
    Scenario: point() creates tupes with w=1
    '''
    p = tuple.point(4, -4, 3)
    assert p == tuple.Tuple(4, -4, 3, 1)


def test_vector():
    '''
    Scenario: vector() creates tuples with w=0
    '''
    v = tuple.vector(4, -4, 3)
    assert v == tuple.Tuple(4, -4, 3, 0)


def test_add_two_tuples():
    '''
    Scenario: Adding two tuples
    '''
    a1 = tuple.Tuple(3, -2, 5, 1)
    a2 = tuple.Tuple(-2, 3, 1, 0)
    assert a1 + a2 == tuple.Tuple(1, 1, 6, 1)


def test_subtract_two_points():
    '''
    Scenario: Subtracting two points
    '''
    p1 = tuple.point(3, 2, 1)
    p2 = tuple.point(5, 6, 7)
    assert p1 - p2 == tuple.vector(-2, -4, -6)


def test_subtract_vector_from_point():
    '''
    Scenario: Subtracting a vector from a point
    '''
    p = tuple.point(3, 2, 1)
    v = tuple.vector(5, 6, 7)
    assert p - v == tuple.point(-2, -4, -6)


def test_subtract_two_vectors():
    '''
    Scenario: Subtracting two vectors
    '''
    v1 = tuple.vector(3, 2, 1)
    v2 = tuple.vector(5, 6, 7)
    assert v1 - v2 == tuple.vector(-2, -4, -6)


def test_subtract_vector_from_zero():
    '''
    Scenario: Subtracting a vector from the zero vector
    '''
    zero = tuple.vector(0, 0, 0)
    v = tuple.vector(1, -2, 3)
    assert zero - v == tuple.vector(-1, 2, -3)


def test_negate_tuple():
    '''
    Scenario: Negating a tuple
    '''
    a = tuple.Tuple(1, -2, 3, -4)
    assert -a == tuple.Tuple(-1, 2, -3, 4)


def test_multiply_tuple_by_scalar():
    '''
    Scenario: Multiplying a tuple by a scalar
    '''
    a = tuple.Tuple(1, -2, 3, -4)
    assert a * 3.5 == tuple.Tuple(3.5, -7, 10.5, -14)


def test_multiply_tuple_by_fraction():
    '''
    Scenario: Multiplying a tuple by a fraction
    '''
    a = tuple.Tuple(1, -2, 3, -4)
    assert a * 0.5 == tuple.Tuple(0.5, -1, 1.5, -2)


def test_divide_tuple_by_scalar():
    '''
    Dividing a tuple by a scalar
    '''
    a = tuple.Tuple(1, -2, 3, -4)
    assert a / 2 == tuple.Tuple(0.5, -1, 1.5, -2)


def test_compute_magnitude_of_vector_1_0_0():
    '''
    Scenario: Computing the magnitude of vector(1, 0, 0)
    '''
    v = tuple.vector(1, 0, 0)
    assert v.magnitude() == 1


def test_compute_magnitude_of_vector_0_1_0():
    '''
    Scenario: Computing the magnitude of vector(0, 1, 0)
    '''
    v = tuple.vector(0, 1, 0)
    assert v.magnitude() == 1


def test_compute_magnitude_of_vector_0_0_1():
    '''
    Scenario: Computing the magnitude of vector(0, 0, 1)
    '''
    v = tuple.vector(0, 0, 1)
    assert v.magnitude() == 1


def test_compute_magnitude_of_vector_1_2_3():
    '''
    Scenario: Computing the magnitude of vector(1, 2, 3)
    '''
    v = tuple.vector(1, 2, 3)
    assert v.magnitude() == math.sqrt(14)


def test_compute_magnitude_of_vector_negative_1_2_3():
    '''
    Scenario: Computing the magnitude of vector(-1, -2, -3)
    '''
    v = tuple.vector(-1, -2, -3)
    assert v.magnitude() == math.sqrt(14)