import pytest
from trtc import Canvas, color


def test_creating_canvas():
    '''
    Scenario: Creating a canvas
    '''
    c = Canvas(10, 20)
    assert c.width == 10
    assert c.height == 20
    for i in range(0, 10):
        for j in range(0, 20):
            assert c.pixels[i][j] == color(0, 0, 0)


def test_writing_pixels_to_canvas():
    '''
    Scenario: Writing pixels to a canvas
    '''
    c = Canvas(10, 20)
    red = color(1, 0, 0)
    c.write_pixel(2, 3, red)
    assert c.pixel_at(2, 3) == red


def test_constructing_ppm_header():
    '''
    Scenario: Constructing the PPM header
    '''
    c = Canvas(5, 3)
    ppm_header = '\n'.join(c.canvas_to_ppm().splitlines()[:3])
    assert ppm_header == 'P3\n5 3\n255'


def test_constructing_ppm_pixel_data():
    '''
    Scenario: Constructing the PPM pixel data
    '''
    c = Canvas(5, 3)
    c1 = color(1.5, 0, 0)
    c2 = color(0, 0.5, 0)
    c3 = color(-0.5, 0, 1)
    c.write_pixel(0, 0, c1)
    c.write_pixel(2, 1, c2)
    c.write_pixel(4, 2, c3)
    ppm = c.canvas_to_ppm()
    result = "P3\n5 3\n255\n" + \
        "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n" + \
        "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n" + \
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255\n"
    assert ppm == result


def test_split_long_lines_in_ppm():
    '''
    Scenario: Splitting long line in PPM files
    '''
    c = Canvas(10, 2)
    for i in range(10):
        for j in range(2):
            c.write_pixel(i, j, color(1, 0.8, 0.6))

    result = "P3\n10 2\n255\n" + \
        "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n" + \
        "153 255 204 153 255 204 153 255 204 153 255 204 153\n" + \
        "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n" + \
        "153 255 204 153 255 204 153 255 204 153 255 204 153\n"
    assert c.canvas_to_ppm() == result


def test_ppm_terminated_by_newline():
    """
    Scenario: PPM files are terminated by a newline character
    """
    c = Canvas(5, 3)
    ppm = c.canvas_to_ppm()
    assert ppm[-1] == '\n'
