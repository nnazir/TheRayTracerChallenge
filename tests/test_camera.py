from math import pi, sqrt
from trtc.utils import float_equal
from trtc.tuple import point, vector, color
from trtc.matrix import Matrix
from trtc.camera import Camera
from trtc.world import World


def test_construct_camera():
    '''
    Scenario: Constructing a camera
    '''
    hsize = 160
    vsize = 120
    field_of_view = pi/2
    c = Camera(hsize, vsize, field_of_view)
    assert c.hsize == hsize
    assert c.vsize == vsize
    assert c.field_of_view == field_of_view
    assert c.transform == Matrix.identity_matrix()


def test_pixel_size_horizontal_canvas():
    '''
    Scenario: The pixel size for a horizontal canvas
    '''
    c = Camera(200, 125, pi/2)
    assert float_equal(c.pixel_size, 0.01)


def test_pixel_size_vertical_canvas():
    '''
    Scenario: The pixel size for a vertical canvas
    '''
    c = Camera(125, 200, pi/2)
    assert float_equal(c.pixel_size, 0.01)


def test_ray_through_canvas_center():
    '''
    Scenario: Constructing a ray through the center of the canvas
    '''
    c = Camera(201, 101, pi/2)
    r = c.ray_for_pixel(100, 50)
    assert r.origin == point(0, 0, 0)
    assert r.direction == vector(0, 0, -1)


def test_ray_through_canvas_corner():
    '''
    Scenario: Constructing a ray through a corner of the canvas
    '''
    c = Camera(201, 101, pi/2)
    r = c.ray_for_pixel(0, 0)
    assert r.origin == point(0, 0, 0)
    assert r.direction == vector(0.66519, 0.33259, -0.66851)


def test_ray_transformed_camera():
    '''
    Scenario: Constructing a ray when the camera is transformed
    '''
    c = Camera(201, 101, pi/2)
    c.transform = Matrix.rotation_y(pi/4) * Matrix.translation(0, -2, 5)
    r = c.ray_for_pixel(100, 50)
    assert r.origin == point(0, 2, -5)
    assert r.direction == vector(sqrt(2)/2, 0, -sqrt(2)/2)


def test_render_world_with_camera():
    '''
    Scenario: Rendering a world with a camera
    '''
    w = World()
    w.default_world()
    c = Camera(11, 11, pi/2)
    scene_from = point(0, 0, -5)
    scene_to = point(0, 0, 0)
    up = vector(0, 1, 0)
    c.transform = Matrix.view_transform(scene_from, scene_to, up)
    image = c.render(w)
    assert image.pixel_at(5, 5) == color(0.38066, 0.47583, 0.2855)
