from trtc import material
from trtc.tuple import point, vector
from trtc import color
from trtc.material import Material
from trtc.light import PointLight
from trtc.pattern import StripePattern
from trtc.sphere import Sphere
from math import sqrt


def test_default_material():
    '''
    Scenario: The default material
    '''
    m = Material()
    assert m.color == color(1, 1, 1)
    assert m.ambient == 0.1
    assert m.diffuse == 0.9
    assert m.specular == 0.9
    assert m.shininess == 200.0


def test_lighting_between_light_surface():
    '''
    Scenario: Lighting with the eye between the light and the surface
    '''
    m = Material()
    s = Sphere()
    position = point(0, 0, 0)
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 0, -10), color(1, 1, 1))
    result = m.lighting(s, light, position, eyev, normalv)
    assert result == color(1.9, 1.9, 1.9)


def test_lighting_between_light_surface_45deg():
    '''
    Scenario: Lighting with the eye between light and surface, eye offset 45 degrees
    '''
    m = Material()
    s = Sphere()
    position = point(0, 0, 0)
    eyev = vector(0, sqrt(2)/2, -sqrt(2)/2)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 0, -10), color(1, 1, 1))
    result = m.lighting(s, light, position, eyev, normalv)
    assert result == (color(1.0, 1.0, 1.0))


def test_lighting_eye_opposite_surface():
    '''
    Scenario: Lighting with eye opposite surface, light offset 45 degrees
    '''
    m = Material()
    s = Sphere()
    position = point(0, 0, 0)
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 10, -10), color(1, 1, 1))
    result = m.lighting(s, light, position, eyev, normalv)
    assert result == color(0.7364, 0.7364, 0.7364)


def test_lighting_with_eye_at_reflection():
    '''
    Scenario: Lighting with eye in the path of the reflection vector
    '''
    m = Material()
    s = Sphere()
    position = point(0, 0, 0)
    eyev = vector(0, -sqrt(2)/2, -sqrt(2)/2)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 10, -10), color(1, 1, 1))
    result = m.lighting(s, light, position, eyev, normalv)
    assert result == color(1.6364, 1.6364, 1.6364)


def test_lighting_with_light_behind_surface():
    '''
    Scenario: Lighting with the light behind the surface
    '''
    m = Material()
    s = Sphere()
    position = point(0, 0, 0)
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 0, 10), color(1, 1, 1))
    result = m.lighting(s, light, position, eyev, normalv)
    assert result == color(0.1, 0.1, 0.1)


def test_lighting_surface_shadow():
    '''
    Scenario: Lighting with the surface in shadow
    '''
    m = Material()
    s = Sphere()
    position = point(0, 0, 0)
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 0, -10), color(1, 1, 1))
    in_shadow = True
    result = m.lighting(s, light, position, eyev, normalv, in_shadow)
    assert result == color(0.1, 0.1, 0.1)


def test_lighting_with_pattern():
    '''
    Scenario: Lighting with a pattern applied
    '''
    m = Material()
    s = Sphere()
    m.pattern = StripePattern(color(1, 1, 1), color(0, 0, 0))
    m.ambient = 1
    m.diffuse = 0
    m.specular = 0
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 0, -10), color(1, 1, 1))
    c1 = m.lighting(s, light, point(0.9, 0, 0), eyev, normalv, False)
    c2 = m.lighting(s, light, point(1.1, 0, 0), eyev, normalv, False)
    assert c1 == color(1, 1, 1)
    assert c2 == color(0, 0, 0)
