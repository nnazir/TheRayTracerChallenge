from trtc.matrix import Matrix
from trtc.tuple import color, point, vector
from trtc.light import PointLight
from trtc.material import Material
from trtc.sphere import Sphere
from trtc.world import World
from trtc.ray import Ray


def test_creating_world():
    '''
    Scenario: Creating a world
    '''
    w = World()
    assert w.objects == []
    assert w.light == None


def test_default_world():
    '''
    Scenario: The default world
    '''
    light = PointLight(point(-10, 10, -10), color(1, 1, 1))
    s1 = Sphere()
    s1.material.color = color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    s2 = Sphere()
    s2.transform = Matrix.scaling(0.5, 0.5, 0.5)
    w = World()
    w.default_world()
    assert w.light == light
    assert s1 in w
    assert s2 in w


def test_intersect_world_ray():
    '''
    Scenario: Intersect a world with a ray
    '''
    w = World()
    w.default_world()
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    xs = w.intersect_world(r)
    assert xs.count == 4
    assert xs.intersections[0].t == 4
    assert xs.intersections[1].t == 4.5
    assert xs.intersections[2].t == 5.5
    assert xs.intersections[3].t == 6
