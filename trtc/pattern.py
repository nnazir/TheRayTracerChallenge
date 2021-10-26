import math
from trtc.tuple import color, point
from trtc.matrix import Matrix
from abc import ABC


class Pattern(ABC):
    def __init__(self, color_a=None, color_b=None) -> None:
        super().__init__()
        self.color_a = color_a
        self.color_b = color_b
        self.transform = Matrix.identity_matrix()

    def pattern_at_shape(self, shape, world_point):
        object_point = shape.transform.inverse() * world_point
        pattern_point = self.transform.inverse() * object_point
        return self.pattern_at(pattern_point)


class TestPattern(Pattern):
    def pattern_at(self, p: point) -> color:
        return color(p.x, p.y, p.z)


class StripePattern(Pattern):
    def pattern_at(self, p: point) -> color:
        ''' Return the appropriate color for the pattern and point '''
        if math.floor(p.x) % 2 == 0:
            return self.color_a
        return self.color_b


class GradientPattern(Pattern):
    def pattern_at(self, p: point):
        distance = self.color_b - self.color_a
        fraction = p.x - math.floor(p.x)

        return self.color_a + distance * fraction


class RingPattern(Pattern):
    def pattern_at(self, p: point) -> color:
        if math.floor(math.sqrt(pow(p.x, 2) + pow(p.x, 2))) // 2 == 0:
            return self.color_a
        return self.color_b
