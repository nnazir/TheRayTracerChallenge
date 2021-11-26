from trtc.tuple import point, vector
from trtc.ray import Ray
from trtc.cube import Cube


def test_ray_intersect_cube():
    ''' Scenario Outline: A ray intersects a cube  '''
    c = Cube()

    tests = [
        [point(5, 0.5, 0), vector(-1, 0, 0), 4, 6],     # +x
        [point(-5, 0.5, 0), vector(1, 0, 0), 4, 6],     # -x
        [point(0.5, 5, 0), vector(0, -1, 0), 4, 6],     # +y
        [point(0.5, -5, 0), vector(0, 1, 0), 4, 6],     # -y
        [point(0.5, 0, 5), vector(0, 0, -1), 4, 6],     # +z
        [point(0.5, 0, -5), vector(0, 0, 1), 4, 6],     # -z
        [point(0, 0.5, 0), vector(0, 0, 1), -1, 1],     # inside
    ]

    for t in tests:
        r = Ray(t[0], t[1])
        xs = c.local_intersect(r)
        assert xs.count == 2
        assert xs.intersections[0].t == t[2]
        assert xs.intersections[1].t == t[3]


def test_ray_misses_cube():
    '''  Scenario Outline: A ray misses a cube  '''
    c = Cube()
    tests = [
        [point(-2, 0, 0), vector(0.2673, 0.5345, 0.8018)],
        [point(0, -2, 0), vector(0.8018, 0.2673, 0.5345)],
        [point(0, 0, -2), vector(0.5345, 0.8018, 0.2673)],
        [point(2, 0, 2), vector(0, 0, -1)],
        [point(0, 2, 2), vector(0, -1, 0)],
        [point(2, 2, 0), vector(-1, 0, 0)],
    ]

    for t in tests:
        r = Ray(t[0], t[1])
        xs = c.local_intersect(r)
        assert xs.count ==  0
