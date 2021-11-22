import math
from typing import Pattern
import pytest
from trtc.matrix import Matrix
from trtc.tuple import color, point, vector
from trtc.light import PointLight
from trtc.material import Material
from trtc.sphere import Sphere
from trtc.plane import Plane
from trtc.world import World
from trtc.ray import Ray
from trtc.intersection import Computations, Intersection, IntersectionList
from trtc.pattern import TestPattern


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


def test_no_shadow_no_collinear_point_light():
    '''
    Scenario: There is no shadow when nothing is collinear with
    point and light
    '''
    w = World()
    w.default_world()
    p = point(0, 10, 0)
    assert w.is_shadowed(p) == False


def test_shadow_object_between_point_light():
    '''
    Scenario: The shadow when an object is between the point and
    the light
    '''
    w = World()
    w.default_world()
    p = point(10, -10, 10)
    assert w.is_shadowed(p) == True


def test_no_shadow_object_behind_light():
    '''
    Scenario: There is no shadow when an object is behind the light
    '''
    w = World()
    w.default_world()
    p = point(-20, 20, -20)
    assert w.is_shadowed(p) == False


def test_no_shadow_object_behind_point():
    '''
    Scenario: There is no shadow when an object is behind the point
    '''
    w = World()
    w.default_world()
    p = point(-2, 2, -2)
    w.is_shadowed(p) == False


def test_shade_hit_intersection_in_shadow():
    '''
    Scenario: shade_hit() is given an intersection in shadow
    '''
    w = World()
    w.default_world()
    w.light = PointLight(point(0, 0, -10), color(1, 1, 1))
    s1 = Sphere()
    w.objects.append(s1)
    s2 = Sphere()
    s2.transform = Matrix.translation(0, 0, 10)
    w.objects.append(s2)
    r = Ray(point(0, 0, 5), vector(0, 0, 1))
    i = Intersection(4, s2)
    comps = i.prepare_computations(r)
    c = w.shade_hit(comps)
    assert c == color(0.1, 0.1, 0.1)


def test_reflected_color_nonreflective_material():
    '''  Scenario: The reflected color for a nonreflective material
         Show that when a ray strikes a nonreflective surrface, the
         reflected_color function returns the color black.
    '''
    w = World()
    w.default_world()
    r = Ray(point(0, 0, 0), vector(0, 0, 1))
    shape = w.objects[1]
    shape.material.ambient = 1
    i = Intersection(1, shape)
    comps = i.prepare_computations(r)
    c = w.reflected_color(comps)
    assert c == color(0, 0, 0)


def test_reflected_color_reflective_material():
    '''  Scenario: The reflected color for a reflective material
         Show that reflected_color returns the color via reflection when the
         struck surface is reflective.
    '''
    w = World()
    w.default_world()
    shape = Plane()
    shape.material.reflective = 0.5
    shape.transform = Matrix.translation(0, -1, 0)
    w.objects.append(shape)
    r = Ray(point(0, 0, -3), vector(0, -math.sqrt(2)/2, math.sqrt(2)/2))
    i = Intersection(math.sqrt(2), shape)
    comps = i.prepare_computations(r)
    c = w.reflected_color(comps)
    # Below color values slightly different than the book
    assert c == color(0.19033, 0.23791, 0.14274)


def test_shade_hit_reflective_material():
    '''  Scenario: The shade_hit() with a reflective material
         Show that shade_hit incorporates teh reflected color into the
         final color.
    '''
    w = World()
    w.default_world()
    shape = Plane()
    shape.material.reflective = 0.5
    shape.transform = Matrix.translation(0, -1, 0)
    w.objects.append(shape)
    r = Ray(point(0, 0, -3), vector(0, -math.sqrt(2)/2, math.sqrt(2)/2))
    i = Intersection(math.sqrt(2), shape)
    comps = i.prepare_computations(r)
    c = w.shade_hit(comps)
    # Below color values slightly different than the book
    assert c == color(0.87676, 0.92434, 0.82918)


def test_mutually_reflective_surfaces():
    '''  Scenario: color_at() with mutually reflective surfaces
         Show that your code handles infinite recursion caused by two objects
         that mutually reflect rays between themselves.
    '''
    w = World()
    w.default_world()
    w.light = PointLight(point(0, 0, 0), color(1, 1, 1))
    lower = Plane()
    lower.material.reflective = 1.0
    lower.transform = Matrix.translation(0, -1, 0)
    w.objects.append(lower)
    upper = Plane()
    upper.material.reflective = 1.0
    upper.transform = Matrix.translation(0, 1, 0)
    w.objects.append(upper)
    r = Ray(point(0, 0, 0), vector(0, 1, 0))
    with pytest.raises(RecursionError):
        w.color_at(r)


def test_reflected_color_max_recursion():
    '''  Scenario: The reflected color at the maximum recursive depth
         Show that reflected_color returns without effect when invoked at
         the limit of its recursive threshold.
    '''
    w = World()
    w.default_world()
    shape = Plane()
    shape.material.reflective = 0.5
    shape.transform = Matrix.translation(0, -1, 0)
    w.objects.append(shape)
    r = Ray(point(0, 0, -3), vector(0, -math.sqrt(2)/2, math.sqrt(2)/2))
    i = Intersection(math.sqrt(2), shape)
    comps = i.prepare_computations(r)
    c = w.reflected_color(comps, 0)
    assert c == color(0, 0, 0)


def test_refracted_color_opaque_surface():
    '''  Scenario: The refracted color with an opaque surface  '''
    w = World()
    w.default_world()
    shape = w.objects[0]
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    xs = IntersectionList()
    xs.intersections.append(Intersection(4, shape))
    xs.intersections.append(Intersection(6, shape))
    comps = xs.intersections[0].prepare_computations(r, xs)
    c = w.refracted_color(comps, 5)
    assert c == color(0, 0, 0)


def test_refracted_color_max_recursive_depth():
    '''  Scenario: The refracted color at the maximum recursive depth  '''
    w = World()
    w.default_world()
    shape = w.objects[0]
    shape.material.transparency = 1.0
    shape.material.refractive_index = 1.5
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    xs = IntersectionList(Intersection(4, shape), Intersection(6, shape))
    comps = xs.intersections[0].prepare_computations(r, xs)
    c = w.refracted_color(comps, 0)
    assert c == color(0, 0, 0)


def test_refracted_color_total_internal_refraction():
    '''  Scenario: The refracted color under totla internal reflection  '''
    w = World()
    w.default_world()
    shape = w.objects[0]
    shape.material.transparency = 1.0
    shape.material.refractive_index = 1.5
    r = Ray(point(0, 0, math.sqrt(2)/2), vector(0, 1, 0))
    xs = IntersectionList()
    xs.intersections.append(Intersection(-math.sqrt(2)/2, shape))
    xs.intersections.append(Intersection(math.sqrt(2)/2, shape))
    comps = xs.intersections[1].prepare_computations(r, xs)
    c = w.refracted_color(comps, 5)
    assert c == color(0, 0, 0)


def test_refracted_color_with_refracted_ray():
    '''  Scenario: The refracted color with a refracted ray  '''
    w = World()
    w.default_world()
    A = w.objects[0]
    A.material.ambient = 1.0
    A.material.pattern = TestPattern()
    B = w.objects[1]
    B.material.transparency = 1.0
    B.material.refractive_index = 1.5
    r = Ray(point(0, 0, 0.1), vector(0, 1, 0))
    xs = IntersectionList()
    xs.intersections.append(Intersection(-0.9899, A))
    xs.intersections.append(Intersection(-0.4899, B))
    xs.intersections.append(Intersection(0.4899, B))
    xs.intersections.append(Intersection(0.9899, A))
    comps = xs.intersections[2].prepare_computations(r, xs)
    c = w.refracted_color(comps, 5)
    assert c == color(0, 0.99887, 0.04722)


def test_shade_hit_with_transparent_material():
    '''  Scenario: shade_hit() with a transparent material  '''
    w = World()
    w.default_world()
    floor = Plane()
    floor.transform = Matrix.translation(0, -1, 0)
    floor.material.transparency = 0.5
    floor.material.refractive_index = 1.5

    ball = Sphere()
    ball.material.color = color(1, 0, 0)
    ball.material.ambient = 0.5
    ball.transform = Matrix.translation(0, -3.5, -0.5)
    w.objects.append(floor)
    w.objects.append(ball)
    r = Ray(point(0, 0, -3), vector(0, -math.sqrt(2)/2, math.sqrt(2)/2))
    xs = IntersectionList(Intersection(math.sqrt(2), floor))
    comps = xs.intersections[0].prepare_computations(r, xs)
    c = w.shade_hit(comps, 5)
    assert c == color(0.93642, 0.68642, 0.68642)


def test_shade_hit_reflective_transparent():
    '''  Scenario: shade_hit() with a reflective, transparent material  '''
    w = World()
    w.default_world()
    r = Ray(point(0, 0, -3), vector(0, -math.sqrt(2)/2, math.sqrt(2)/2))
    floor = Plane()
    floor.transform = Matrix.translation(0, -1, 0)
    floor.material.reflective = 0.5
    floor.material.transparency = 0.5
    floor.material.refractive_index = 1.5
    ball = Sphere()
    ball.material.color = color(1, 0, 0)
    ball.material.ambient = 0.5
    ball.transform = Matrix.translation(0, -3.5, -0.5)
    w.objects.append(floor)
    w.objects.append(ball)
    xs = IntersectionList(Intersection(math.sqrt(2), floor))
    comps = xs.intersections[0].prepare_computations(r, xs)
    c = w.shade_hit(comps, 5)
    assert c == color(0.93391, 0.69643, 0.69243)
