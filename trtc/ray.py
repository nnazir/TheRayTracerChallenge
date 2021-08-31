class Ray():
    def __init__(self, origin, direction) -> None:
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction * t
