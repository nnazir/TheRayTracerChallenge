from trtc import point, vector
from trtc import Ray

def test_create_query_ray():
    '''
    Scenario: Creating and querying a ray
    '''
    origin = point(1, 2, 3)
    direction = vector(4, 5, 6)
    r = Ray(origin, direction)
    assert r.origin == origin
    assert r.direction == direction
