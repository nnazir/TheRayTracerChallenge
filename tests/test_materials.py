from trtc import color
from trtc.material import Material


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
