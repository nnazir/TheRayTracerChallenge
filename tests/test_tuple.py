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
