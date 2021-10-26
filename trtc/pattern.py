import math
from trtc.tuple import color, point
from trtc.matrix import Matrix
from abc import ABC


class Pattern(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.transform = Matrix.identity_matrix()

    def pattern_at_shape(self, shape, world_point):
        object_point = shape.transform.inverse() * world_point
        pattern_point = self.transform.inverse() * object_point
        return self.pattern_at(pattern_point)


class TestPattern(Pattern):
    def pattern_at(self, p: point) -> color:
        return color(p.x, p.y, p.z)


class StripePattern(Pattern):
    def __init__(self, stripe_a, stripe_b) -> None:
        self.a = stripe_a
        self.b = stripe_b
        self.transform = Matrix.identity_matrix()

    def pattern_at(self, p: point) -> color:
        ''' Return the appropriate color for the pattern and point '''
        if math.floor(p.x) % 2 == 0:
            return self.a
        return self.b


class GradientPattern(Pattern):
    def __init__(self, color_a, color_b) -> None:
        super().__init__()
        self.color_a = color_a
        self.color_b = color_b

    def pattern_at(self, p: point):
        distance = self.color_b - self.color_a
        fraction = p.x - math.floor(p.x)

        return self.color_a + distance * fraction
