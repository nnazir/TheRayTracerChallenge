from trtc.sphere import Sphere
from trtc.intersection import Intersection, IntersectionList


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
