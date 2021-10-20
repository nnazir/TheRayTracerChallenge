import math
from trtc.tuple import color, point


class StripePattern():
    def __init__(self, stripe_a, stripe_b) -> None:
        self.a = stripe_a
        self.b = stripe_b

    def stripe_at(self, p: point) -> color:
        ''' Return the appropriate color for the pattern and point '''
        if math.floor(p.x) % 2 == 0:
            return self.a
        return self.b
