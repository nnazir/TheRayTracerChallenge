import math
from trtc.tuple import color, point
from trtc.matrix import Matrix

class StripePattern():
    def __init__(self, stripe_a, stripe_b) -> None:
        self.a = stripe_a
        self.b = stripe_b
        self.transform = Matrix.identity_matrix()

    def stripe_at(self, p: point) -> color:
        ''' Return the appropriate color for the pattern and point '''
        if math.floor(p.x) % 2 == 0:
            return self.a
        return self.b

    def stripe_at_object(self, obj, world_point):
        object_point = obj.transform.inverse() * world_point
        pattern_point = self.transform.inverse() * object_point

        return self.stripe_at(pattern_point)
