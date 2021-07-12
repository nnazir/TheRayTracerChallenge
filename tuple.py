from utils import float_equal


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


class Point(Tuple):
    def __init__(self, x=None, y=None, z=None, w=None):
        super().__init__(x, y, z, 1)

    def __add__(self, other):
        t = super().__add__(other)
        if t.w == 0:
            return Vector(t.x, t.y, t.z, t.w)
        elif t.w == 1:
            return Point(t.x, t.y, t.z, t.w)


class Vector(Tuple):
    def __init__(self, x=None, y=None, z=None, w=None):
        super().__init__(x, y, z, 0)

    def __add__(self, other):
        t = super().__add__(other)
        if t.w == 0:
            return Vector(t.x, t.y, t.z, t.w)
        elif t.w == 1:
            return Point(t.x, t.y, t.z, t.w)


def point(x, y, z):
    return Point(x, y, z)


def vector(x, y, z):
    return Vector(x, y, z)
