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


def test_ray_intersect_sphere_at_two_points():
    '''
    Scenario: A ray intersects a sphere at two points
    '''
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert len(xs) == 2
    assert xs[0] == 4.0
    assert xs[1] == 6.0


def test_ray_intersect_sphere_at_tangent():
    '''
    Scenario: A ray intersects a sphere at a tangent
    '''
    r = Ray(point(0, 1, -5), vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert len(xs) == 2
    assert xs[0] == 5.0
    assert xs[1] == 5.0


def test_ray_misses_shpere():
    '''
    Scenario: A ray misses a sphere
    '''
    r = Ray(point(0, 2, -5), vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert xs == None


def test_ray_originates_in_sphere():
    '''
    Scenario: A ray originates inside a sphere
    '''
    r = Ray(point(0, 0, 0), vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert len(xs) == 2
    assert xs[0] == -1.0
    assert xs[1] == 1.0


def test_sphere_behind_ray():
    '''
    Scenario: A sphere is behind a ray
    '''
    r = Ray(point(0, 0, 5), vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert len(xs) == 2
    assert xs[0] == -6.0
    assert xs[1] == -4.0
