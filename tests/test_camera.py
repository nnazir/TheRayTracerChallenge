from math import pi
from trtc.matrix import Matrix
from trtc.camera import Camera
from trtc.utils import float_equal


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
