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


class Point(Tuple):
    def __init__(self, x=None, y=None, z=None, w=None):
        super().__init__(x, y, z, 0)


class Vector(Tuple):
    def __init__(self, x=None, y=None, z=None, w=None):
        super().__init__(x, y, z, 1)


def point(x, y, z):
    return Point(x, y, z)


def vector(x, y, z):
    return Vector(x, y, z)
