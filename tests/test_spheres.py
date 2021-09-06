from trtc import Ray, Sphere, point, vector


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
