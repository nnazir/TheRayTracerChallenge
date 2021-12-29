from trtc.tuple import point, vector
from trtc.matrix import Matrix
from trtc.shape import TestShape
from trtc.ray import Ray
from trtc.group import Group
from trtc.sphere import Sphere


def test_create_group():
    '''  Scenario: Creating a new group  '''
    g = Group()
    g.transform = Matrix.identity_matrix()
    assert g.shapes == []


def test_add_child_to_group():
    '''  Scenario: Adding a child to a group  '''
    g = Group()
    s = TestShape()
    g.add_child(s)
    assert g.shapes != []
    assert s in g.shapes
    assert s.parent == g


def test_intersect_ray_empty_group():
    '''  Scenario: Intersecting a ray with an empty group  '''
    g = Group()
    r = Ray(point(0, 0, 0), vector(0, 0, 1))
    xs = g.local_intersect(r)
    assert not xs.intersections


def test_intersect_ray_nonempty_group():
    '''  Scenario: Intersecting a ray with a nonempty group  '''
    g = Group()
    s1 = Sphere()
    s2 = Sphere()
    s2.transform = Matrix.translation(0, 0, -3)
    s3 = Sphere()
    s3.transform = Matrix.translation(5, 0, 0)
    g.add_child(s1)
    g.add_child(s2)
    g.add_child(s3)
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    xs = g.local_intersect(r)
    assert xs.count == 4
    assert xs.intersections[0].object == s2
    assert xs.intersections[1].object == s2
    assert xs.intersections[2].object == s1
    assert xs.intersections[3].object == s1


def test_intersect_transformed_group():
    '''  Scenario: Intersecting a transformed group  '''
    g = Group()
    g.transform = Matrix.scaling(2, 2, 2)
    s = Sphere()
    s.transform = Matrix.translation(5, 0, 0)
    g.add_child(s)
    r = Ray(point(10, 0, -10), vector(0, 0, 1))
    xs = g.intersect(r)
    assert xs.count == 2
