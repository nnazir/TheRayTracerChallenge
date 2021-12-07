from trtc.utils import float_equal
from trtc.tuple import point, vector
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
