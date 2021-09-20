from trtc.matrix import Matrix
from trtc.tuple import color, point, vector
from trtc.light import PointLight
from trtc.material import Material
from trtc.sphere import Sphere
from trtc.world import World
from trtc.ray import Ray
from trtc.intersection import Intersection


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


def test_shade_intersection():
    '''
    Scenario: Shading an intersection
    '''
    w = World()
    w.default_world()
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    shape = w.objects[0]
    i = Intersection(4, shape)
    comps = i.prepare_computations(r)
    c = w.shade_hit(comps)
    assert c == color(0.38066, 0.47583, 0.2855)


def test_shade_intersection_inside():
    '''
    Scenario: Shading an intersection from the inside
    '''
    w = World()
    w.default_world()
    w.light = PointLight(point(0, 0.25, 0), color(1, 1, 1))
    r = Ray(point(0, 0, 0), vector(0, 0, 1))
    shape = w.objects[1]
    i = Intersection(0.5, shape)
    comps = i.prepare_computations(r)
    c = w.shade_hit(comps)
    assert c == color(0.90498, 0.90498, 0.90498)


def test_color_ray_misses():
    '''
    Scenario: The color when a ray misses
    '''
    w = World()
    w.default_world()
    r = Ray(point(0, 0, -5), vector(0, 1, 0))
    c = w.color_at(r)
    assert c == color(0, 0, 0)


def test_color_ray_hits():
    '''
    Scenario: The color when a ray hits
    '''
    w = World()
    w.default_world()
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    c = w.color_at(r)
    assert c == color(0.38066, 0.47583, 0.2855)


def test_color_intersection_behind_ray():
    '''
    Scenario: The color with an intersection behind the ray
    '''
    w = World()
    w.default_world()
    outer = w.objects[0]
    outer.material.ambient = 1
    inner = w.objects[1]
    inner.material.ambient = 1
    r = Ray(point(0, 0, 0.75), vector(0, 0, -1))
    c = w.color_at(r)
    assert c == inner.material.color
