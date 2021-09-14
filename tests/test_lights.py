from trtc import color
from trtc.tuple import point
from trtc.light import PointLight


def test_point_light_has_position_intensity():
    '''
    Scenario: A point light has a position and intensity
    '''
    intensity = color(1, 1, 1)
    position = point(0, 0, 0)
    light = PointLight(position, intensity)
    assert light.position == position
    assert light.intensity == intensity
