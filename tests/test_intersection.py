import math
from trtc.utils import EPSILON
from trtc.matrix import Matrix
from trtc.sphere import Sphere, glass_sphere
from trtc.ray import Ray
from trtc.intersection import Intersection, IntersectionList
from trtc.tuple import point, vector
from trtc.plane import Plane


def test_intersection_encapsulate_t_and_object():
    '''
    Scenario: An intersection encapsulates t and object
    '''
    s = Sphere()
    i = Intersection(3.5, s)
    assert i.t == 3.5
    assert i.object == s


def test_aggregating_intersections():
    '''
    Scenario: Aggregating intersections
    '''
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = IntersectionList(i1, i2)
    assert xs.count == 2
    assert xs.intersections[0].t == 1
    assert xs.intersections[1].t == 2


def test_hit_all_positive_t():
    '''
    Scenario: The hit, when all intersections have positive t
    '''
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = IntersectionList(i2, i1)
    i = xs.hit()
    assert i == i1


def test_hit_some_negative_t():
    '''
    Scenario: The hit, when some intersections have negative t
    '''
    s = Sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(1, s)
    xs = IntersectionList(i2, i1)
    i = xs.hit()
    assert i == i2


def test_hit_all_test_hit_all_negative_t():
    '''
    Scenario: The hit, when all intersections have negative t
    '''
    s = Sphere()
    i1 = Intersection(-2, s)
    i2 = Intersection(-1, s)
    xs = IntersectionList(i2, i1)
    i = xs.hit()
    assert i is None


def test_hit_always_lowest_nonnegative():
    '''
    Scenario: The hit is always the lowest nonnegative intersection
    '''
    s = Sphere()
    i1 = Intersection(5, s)
    i2 = Intersection(7, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)
    xs = IntersectionList(i1, i2, i3, i4)
    i = xs.hit()
    assert i == i4


def test_precompute_intersection_state():
    '''
    Precomputing the state of an intersection
    '''
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    comps = i.prepare_computations(r)
    assert comps.t == i.t
    assert comps.object == i.object
    assert comps.point == point(0, 0, -1)
    assert comps.eyev == vector(0, 0, -1)
    assert comps.normalv == vector(0, 0, -1)


def test_hit_intersection_outside():
    '''
    Scenario: The hit, when an intersection occurs on the outside
    '''
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    comps = i.prepare_computations(r)
    assert comps.inside == False


def test_hit_intersection_inside():
    '''
    Scenario: The hit, when an intersection occurs on the inside
    '''
    r = Ray(point(0, 0, 0), vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(1, shape)
    comps = i.prepare_computations(r)
    assert comps.point == point(0, 0, 1)
    assert comps.eyev == vector(0, 0, -1)
    assert comps.inside == True
    # normal would have been (0, 0, 1), but is inverted
    comps.normalv == vector(0, 0, -1)


def test_hit_offsets_point():
    '''
    Scenario: The hit should offset the point
    '''
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    shape = Sphere()
    shape.transform = Matrix.translation(0, 0, 1)
    i = Intersection(5, shape)
    comps = i.prepare_computations(r)
    assert comps.over_point.z < -EPSILON/2
    assert comps.point.z > comps.over_point.z


def test_precompute_reflection_vector():
    '''  Scenario: Precomputing the reflection vector  '''
    shape = Plane()
    r = Ray(point(0, 1, -1), vector(0, -math.sqrt(2)/2, math.sqrt(2)/2))
    i = Intersection(math.sqrt(2), shape)
    comps = i.prepare_computations(r)
    assert comps.reflectv == vector(0, math.sqrt(2)/2, math.sqrt(2)/2)


def test_finding_n1_and_n2():
    '''  Scenario: Finding n1 and n2 at various intersections  '''
    A = glass_sphere()
    A.transform = Matrix.scaling(2, 2, 2)
    A.material.refractive_index = 1.5
    B = glass_sphere()
    B.transform = Matrix.translation(0, 0, -0.25)
    B.material.refractive_index = 2.0
    C = glass_sphere()
    C.transform = Matrix.translation(0, 0, 0.25)
    C.material.refractive_index = 2.5
    r = Ray(point(0, 0, -4), vector(0, 0, 1))
    xs = IntersectionList()
    xs.intersections.append(Intersection(2, A))
    xs.intersections.append(Intersection(2.75, B))
    xs.intersections.append(Intersection(3.25, C))
    xs.intersections.append(Intersection(4.75, B))
    xs.intersections.append(Intersection(5.25, C))
    xs.intersections.append(Intersection(6, A))
    # containers = []
    comps0 = xs.intersections[0].prepare_computations(r, xs)
    assert comps0.n1 == 1.0
    assert comps0.n2 == 1.5
    comps1 = xs.intersections[1].prepare_computations(r, xs)
    assert comps1.n1 == 1.5
    assert comps1.n2 == 2.0
    comps2 = xs.intersections[2].prepare_computations(r, xs)
    assert comps2.n1 == 2.0
    assert comps2.n2 == 2.5
    comps3 = xs.intersections[3].prepare_computations(r, xs)
    assert comps3.n1 == 2.5
    assert comps3.n2 == 2.5
    comps4 = xs.intersections[4].prepare_computations(r, xs)
    assert comps4.n1 == 2.5
    assert comps4.n2 == 1.5
    comps5 = xs.intersections[5].prepare_computations(r, xs)
    assert comps5.n1 == 1.5
    assert comps5.n2 == 1.0


def test_computing_under_point():
    '''  Scenario: The under point is offset below the surface  '''
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    shape = glass_sphere()
    shape.transform = Matrix.translation(0, 0, 1)
    i = Intersection(5, shape)
    xs = IntersectionList(i)
    comps = i.prepare_computations(r, xs)
    assert comps.under_point.z > EPSILON/2
    assert comps.point.z < comps.under_point.z
