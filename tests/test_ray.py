from trtc import point, vector
from trtc import Ray, Sphere


def test_create_query_ray():
    '''
    Scenario: Creating and querying a ray
    '''
    origin = point(1, 2, 3)
    direction = vector(4, 5, 6)
    r = Ray(origin, direction)
    assert r.origin == origin
    assert r.direction == direction


def test_compute_point_from_distance():
    '''
    Scenario: Computing a point from a distance
    '''
    r = Ray(point(2, 3, 4), vector(1, 0, 0))
    assert r.position(0) == point(2, 3, 4)
    assert r.position(1) == point(3, 3, 4)
    assert r.position(-1) == point(1, 3, 4)
    assert r.position(2.5) == point(4.5, 3, 4)
