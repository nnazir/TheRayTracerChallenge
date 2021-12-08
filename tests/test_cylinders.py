from trtc.utils import float_equal
from trtc.tuple import Tuple, point, vector
from trtc.ray import Ray
from trtc.cylinder import Cylinder


def test_ray_misses_cylinder():
    '''  Scenario Outline: A ray misses a cylinder  '''
    cyl = Cylinder()
    tests = [
        [point(1, 0, 0), vector(0, 1, 0)],
        [point(0, 0, 0), vector(0, 1, 0)],
        [point(0, 0, -5), vector(1, 1, 1)]
    ]

    for t in tests:
        direction = t[1].normalize()
        r = Ray(t[0], t[1])
        xs = cyl.local_intersect(r)
        assert xs.count == 0


def test_ray_strikes_cylinder():
    '''  Scenario Outline: A ray strikes a cylinder  '''
    cyl = Cylinder()
    tests = [
        # origin,         direction,      t0, t1
        [point(1, 0, -5), vector(0, 0, 1), 5, 5],
        [point(0, 0, -5), vector(0, 0, 1), 4, 6],
        [point(0.5, 0, -5), vector(0.1, 1, 1), 6.80798, 7.08872],
    ]
    for t in tests:
        direction = t[1].normalize()
        r = Ray(t[0], direction)
        xs = cyl.local_intersect(r)
        assert xs.count == 2
        assert float_equal(xs.intersections[0].t, t[2])
        assert float_equal(xs.intersections[1].t, t[3])


def test_cylinder_normal():
    '''  Scenario Outline: Normal vector on a cylinder  '''
    cyl = Cylinder()
    tests = [
        # point, normal
        [point(1, 0, 0), vector(1, 0, 0)],
        [point(0, 5, -1), vector(0, 0, -1)],
        [point(0, -2, 1), vector(0, 0, 1)],
        [point(-1, 1, 0), vector(-1, 0, 0)],
    ]
    for t in tests:
        n = cyl.normal_at(t[0])
        assert n == t[1]


def test_cylinder_default_min_max():
    '''  Scenario: The default minimum and maximum for a cylinder  '''
    cyl = Cylinder()
    assert cyl.minimum == float('-inf')
    assert cyl.maximum == float('inf')


def test_intersect_constrained_cylinder():
    '''  Scenario Outline: Intersecting a constrained cylinder  '''
    cyl = Cylinder()
    cyl.minimum = 1
    cyl.maximum = 2
    tests = [
        [point(0, 1.5, 0), vector(0.1, 1, 0), 0],
        [point(0, 3, -5), vector(0, 0, 1), 0],
        [point(0, 0, -5), vector(0, 0, 1), 0],
        [point(0, 2, -5), vector(0, 0, 1), 0],
        [point(0, 1, -5), vector(0, 0, 1), 0],
        [point(0, 1.5, -2), vector(0, 0, 1), 2],
    ]
    for t in tests:
        direction = t[1].normalize()
        r = Ray(t[0], direction)
        xs = cyl.local_intersect(r)
        assert xs.count == t[2]


def test_default_cylinder_closed():
    '''  Scenario: The default closed value for a cylinder '''
    cyl = Cylinder()
    assert cyl.closed == False


def test_intersect_closed_cylinder_caps():
    '''  Scenario Outline: Intersecting the caps of a closed cylinder  '''
    cyl = Cylinder()
    cyl.minimum = 1
    cyl.maximum = 2
    cyl.closed = True
    tests = [
        [point(0, 3, 0), vector(0, -1, 0), 2],
        [point(0, 3, -2), vector(0, -1, 2), 2],
        [point(0, 4, -2), vector(0, -1, 1), 2],
        [point(0, 0, -2), vector(0, 1, 2), 2],
        [point(0, -1, -2), vector(0, 1, 1), 2],
    ]
    for t in tests:
        direction = t[1].normalize()
        r = Ray(t[0], direction)
        xs = cyl.local_intersect(r)
        assert xs.count == t[2]
