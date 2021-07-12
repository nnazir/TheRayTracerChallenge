import pytest
import tuple


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
