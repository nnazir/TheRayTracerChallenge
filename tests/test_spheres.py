from trtc.matrix import Matrix
from trtc import Ray, Sphere, point, vector


def test_ray_intersect_sphere_at_two_points():
    '''
    Scenario: A ray intersects a sphere at two points
    '''
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert xs.count == 2
    assert xs.intersections[0].t == 4.0
    assert xs.intersections[1].t == 6.0


def test_ray_intersect_sphere_at_tangent():
    '''
    Scenario: A ray intersects a sphere at a tangent
    '''
    r = Ray(point(0, 1, -5), vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert xs.count == 2
    assert xs.intersections[0].t == 5.0
    assert xs.intersections[1].t == 5.0


def test_ray_misses_shpere():
    '''
    Scenario: A ray misses a sphere
    '''
    r = Ray(point(0, 2, -5), vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert xs.count == 0


def test_ray_originates_in_sphere():
    '''
    Scenario: A ray originates inside a sphere
    '''
    r = Ray(point(0, 0, 0), vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert xs.count == 2
    assert xs.intersections[0].t == -1.0
    assert xs.intersections[1].t == 1.0


def test_sphere_behind_ray():
    '''
    Scenario: A sphere is behind a ray
    '''
    r = Ray(point(0, 0, 5), vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert xs.count == 2
    assert xs.intersections[0].t == -6.0
    assert xs.intersections[1].t == -4.0


def test_intersect_sets_object_on_intersection():
    '''
    Scenario: Intersect sets the object on the intersection
    '''
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = Sphere()
    xs = s.intersect(r)
    assert xs.count == 2
    assert xs.intersections[0].object == s
    assert xs.intersections[1].object == s


def test_sphere_default_transformation():
    '''
    Scenario: A sphere's default transformation
    '''
    s = Sphere()
    assert s.transform == Matrix.identity_matrix()


def test_changing_sphere_transformation():
    '''
    Scenario: Changing a sphere's transformation
    '''
    s = Sphere()
    t = Matrix.translation(2, 3, 4)
    s.transform = t
    assert s.transform == t


def test_intersect_scaled_sphere_with_ray():
    '''
    Scenario: Intersecting a scaled sphere with a ray
    '''
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = Sphere()
    s.transform = Matrix.scaling(2, 2, 2)
    xs = s.intersect(r)
    assert xs.count == 2
    assert xs.intersections[0].t == 3
    assert xs.intersections[1].t == 7


def test_intersect_translated_sphere_with_ray():
    '''
    Scenario: Intersecting a translated sphere with a ray
    '''
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = Sphere()
    s.transform = Matrix.translation(5, 0, 0)
    xs = s.intersect(r)
    assert xs.count == 0
