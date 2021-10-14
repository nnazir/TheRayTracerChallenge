from trtc.tuple import point, vector
from trtc.ray import Ray
from trtc.plane import Plane


def test_normal_of_plane():
    '''
    Scenario: The normal of a plane is constant everywhere
    '''
    p = Plane()
    n1 = p.local_normal_at(point(0, 0, 0))
    n2 = p.local_normal_at(point(10, 0, -10))
    n3 = p.local_normal_at(point(-5, 0, 150))
    assert n1 == vector(0, 1, 0)
    assert n2 == vector(0, 1, 0)
    assert n3 == vector(0, 1, 0)


def test_intersect_ray_parallel_to_plane():
    '''
    Scenario: Intersect with a ray parallel to the plane
    '''
    p = Plane()
    r = Ray(point(0, 10, 0), vector(0, 0, 1))
    xs = p.local_intersect(r)
    assert xs is None


def test_intersect_coplanar_ray():
    '''
    Scenario: Intersect with a coplanar ray
    '''
    p = Plane()
    r = Ray(point(0, 0, 0), vector(0, 0, 1))
    xs = p.local_intersect(r)
    assert xs is None


def test_ray_intersect_plane_from_above():
    '''
    Scenario: A ray intersecting a plane from above
    '''
    p = Plane()
    r = Ray(point(0, 1, 0), vector(0, -1, 0))
    xs = p.local_intersect(r)
    assert xs.count == 1
    assert xs.intersections[0].t == 1
    assert xs.intersections[0].object == p


def test_ray_intersect_plane_from_below():
    '''
    Scenario: A ray intersecting a plane from below
    '''
    p = Plane()
    r = Ray(point(0, -1, 0), vector(0, 1, 0))
    xs = p.local_intersect(r)
    assert xs.count == 1
    assert xs.intersections[0].t == 1
    assert xs.intersections[0].object == p
