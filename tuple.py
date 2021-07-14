from utils import float_equal
import math


class Tuple():
    def __init__(self, x=None, y=None, z=None, w=None):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __repr__(self):
        return repr(f'{self.x}, {self.y}, {self.z}, {self.w}')

    def __eq__(self, o: object) -> bool:
        return float_equal(self.x, o.x) and \
            float_equal(self.y, o.y) and \
            float_equal(self.z, o.z) and \
            float_equal(self.w, o.w)

    def __add__(self, other):
        return Tuple(self.x + other.x,
                     self.y + other.y,
                     self.z + other.z,
                     self.w + other.w)

    def __sub__(self, other):
        return Tuple(self.x - other.x,
                     self.y - other.y,
                     self.z - other.z,
                     self.w - other.w)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, other):
        return Tuple(self.x * other,
                     self.y * other,
                     self.z * other,
                     self.w * other)

    def __truediv__(self, other):
        return Tuple(self.x / other,
                     self.y / other,
                     self.z / other,
                     self.w / other)

    def magnitude(self):
        return math.sqrt(self.x ** 2 +
                         self.y ** 2 +
                         self.z ** 2 +
                         self.w ** 2)

    def normalize(self):
        return Tuple(self.x / self.magnitude(),
                     self.y / self.magnitude(),
                     self.z / self.magnitude(),
                     self.w / self.magnitude()
                     )


def point(x, y, z):
    # return Point(x, y, z)
    return Tuple(x, y, z, 1)


def vector(x, y, z):
    # return Vector(x, y, z)
    return Tuple(x, y, z, 0)
