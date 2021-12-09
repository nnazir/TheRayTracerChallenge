from trtc.utils import float_equal
from trtc.tuple import point, vector
from trtc.ray import Ray
from trtc.intersection import Intersection, IntersectionList
from trtc.cone import Cone


def test_ray_intersect_cone():
    '''  Scenario Outline: Intersecting a cone with a ray  '''
    shape = Cone()
    tests = [
        # [point(0, 0, -5), vector(0, 0, 1), 5, 5],
        [point(0, 0, -5), vector(1, 1, 1), 8.66025, 8.66025],
        [point(1, 1, -5), vector(-0.5, -1, 1), 4.55006, 49.44994],
    ]
    for t in tests:
        direction = t[1].normalize()
        r = Ray(t[0], direction)
        xs = shape.local_intersect(r)
        assert xs.count == 2
        assert float_equal(xs.intersections[0].t, t[2])
        assert float_equal(xs.intersections[1].t, t[3])
