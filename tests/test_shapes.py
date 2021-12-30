from math import pi, sqrt
import math
from trtc.tuple import point, vector
from trtc.material import Material
from trtc.matrix import Matrix
from trtc.ray import Ray
from trtc.shape import Shape, TestShape
from trtc.group import Group
from trtc.sphere import Sphere


def test_default_transformation():
    '''
    Scenario: The default transformation
    '''
    s = Shape()
    # s.test_shape()
    assert s.transform == Matrix.identity_matrix()


def test_assign_transformation():
    '''
    Scenario: Assigning a transformation
    '''
    s = Shape()
    # s.test_shape()
    s.transform = Matrix.translation(2, 3, 4)
    assert s.transform == Matrix.translation(2, 3, 4)


def test_default_material():
    '''
    Scenario: The default material
    '''
    s = TestShape()
    m = s.material
    assert isinstance(m, Material)


def test_assign_material():
    '''
    Scenario: Assigning a material
    '''
    s = TestShape()
    m = Material()
    m.ambient = 1
    s.material = m
    assert s.material == m


def test_intersect_scaled_shape_with_ray():
    '''
    Scenario: Intersecting a scaled shape with a ray
    '''
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = TestShape()
    s.transform = Matrix.scaling(2, 2, 2)
    xs = s.intersect(r)
    assert s.saved_ray.origin == point(0, 0, -2.5)
    assert s.saved_ray.direction == vector(0, 0, 0.5)


def test_intersect_translate_shape_with_ray():
    '''
    Scenario: Intersecting a translated shape with a ray
    '''
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = TestShape()
    s.transform = Matrix.translation(5, 0, 0)
    xs = s.intersect(r)
    assert s.saved_ray.origin == point(-5, 0, -5)
    assert s.saved_ray.direction == vector(0, 0, 1)


def test_compute_translate_shape_normal():
    '''
    Scenario: Computing the normal on a translated shape
    '''
    s = TestShape()
    s.transform = Matrix.translation(0, 1, 0)
    n = s.normal_at(point(0, 1.70711, -0.70711))
    assert n == vector(0, 0.70711, -0.70711)


def test_compute_transformed_shape_normal():
    '''
    Scenario: Computing the normal on a transformed shape
    '''
    s = TestShape()
    m = Matrix.scaling(1, 0.5, 1) * Matrix.rotation_z(pi/5)
    s.transform = m
    n = s.normal_at(point(0, sqrt(2)/2, -sqrt(2)/2))
    assert n == vector(0, 0.97014, -0.24254)


def test_shape_parent_attr():
    '''  Scenario: A shape has a parent attribute  '''
    s = TestShape()
    assert s.parent is None


def test_convert_point_from_world_to_object_space():
    '''  Scenario: Converting a point from world to object space  '''
    g1 = Group()
    g1.transform = Matrix.rotation_y(math.pi/2)
    g2 = Group()
    g2.transform = Matrix.scaling(2, 2, 2)
    g1.add_child(g2)
    s = Sphere()
    s.transform = Matrix.translation(5, 0, 0)
    g2.add_child(s)
    p = s.world_to_object(point(-2, 0, -10))
    assert p == point(0, 0, -1)


def test_convert_normal_from_object_to_world_space():
    '''  Scenario: Converting a normal from object to world space  '''
    g1 = Group()
    g1.transform = Matrix.rotation_y(math.pi/2)
    g2 = Group()
    g2.transform = Matrix.scaling(1, 2, 3)
    g1.add_child(g2)
    s = Sphere()
    s.transform = Matrix.translation(5, 0, 0)
    g2.add_child(s)
    n = s.normal_to_world(
        vector(math.sqrt(3)/3, math.sqrt(3)/3, math.sqrt(3)/3))
    assert n == vector(0.28571, 0.42857, -0.85714)
