from . import utils
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
        return utils.float_equal(self.x, o.x) and \
            utils.float_equal(self.y, o.y) and \
            utils.float_equal(self.z, o.z) and \
            utils.float_equal(self.w, o.w)

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

    def dot(self, other):
        return self.x * other.x + self.y * other.y + \
            self.z * other.z + self.w * other.w

    def cross(self, other):
        return vector(self.y * other.z - self.z*other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x
                      )

    def list(self):
        return [self.x, self.y, self.z, self.w]

    def reflect(self, normal):
        return self - normal * 2 * self.dot(normal)


class Color(Tuple):
    def __init__(self, r, g, b, w):
        self.red = r
        self.green = g
        self.blue = b
        self.w = w

    @property
    def red(self):
        return self.x

    @red.setter
    def red(self, value):
        self.x = value

    @property
    def green(self):
        return self.y

    @green.setter
    def green(self, value):
        self.y = value

    @property
    def blue(self):
        return self.z

    @blue.setter
    def blue(self, value):
        self.z = value

    def __mul__(self, other):
        if type(other) == int:
            return Color(self.x * other,
                         self.y * other,
                         self.z * other,
                         self.w * other)
        else:
            return Color(self.x * other.x,
                         self.y * other.y,
                         self.z * other.z,
                         self.w * other.w)


def point(x, y, z):
    # return Point(x, y, z)
    return Tuple(x, y, z, 1)


def vector(x, y, z):
    # return Vector(x, y, z)
    return Tuple(x, y, z, 0)


def color(r, g, b):
    return Color(r, g, b, 0)
