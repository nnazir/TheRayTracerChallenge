import pytest
import tuple


def test_point():
    '''
    Scenario: point() creates tupes with w=1
    '''
    p = tuple.point(4, -4, 3)
    assert p == tuple.Point(4, -4, 3, 1)


def test_vector():
    '''
    Scenario: vector() creates tuples with w=0
    '''
    v = tuple.vector(4, -4, 3)
    assert v == tuple.Vector(4, -4, 3, 0)


def test_add_two_tuples():
    '''
    Scenario: Adding two tuples
    '''
    a1 = tuple.Tuple(3, -2, 5, 1)
    a2 = tuple.Tuple(-2, 3, 1, 0)
    assert a1 + a2 == tuple.Tuple(1, 1, 6, 1)
