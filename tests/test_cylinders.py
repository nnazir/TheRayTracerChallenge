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
