from trtc.matrix import Matrix
from trtc.shape import Shape
from trtc.group import Group


def test_create_group():
    '''  Scenario: Creating a new group  '''
    g = Group()
    g.transform = Matrix.identity_matrix()
    assert g.shapes == []
