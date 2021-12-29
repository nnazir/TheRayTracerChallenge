from trtc.matrix import Matrix
from trtc.shape import Shape, TestShape
from trtc.group import Group


def test_create_group():
    '''  Scenario: Creating a new group  '''
    g = Group()
    g.transform = Matrix.identity_matrix()
    assert g.shapes == []


def test_add_child_to_group():
    '''  Scenario: Adding a child to a group  '''
    g = Group()
    s = TestShape()
    g.add_child(s)
    assert g.shapes != []
    assert s in g.shapes
    assert s.parent == g
