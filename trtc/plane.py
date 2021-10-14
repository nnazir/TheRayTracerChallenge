from .tuple import Tuple, point, vector
from .shape import Shape
from .intersection import Intersection, IntersectionList
from .utils import EPSILON


class Plane(Shape):
    '''
    Assumes a plane on the xz axis
    '''

    def local_normal_at(self, p) -> vector:
        return vector(0, 1, 0)

    def local_intersect(self, ray) -> Intersection:
        if abs(ray.direction.y) < EPSILON:
            return
        t = -ray.origin.y / ray.direction.y
        return IntersectionList(Intersection(t, self))
