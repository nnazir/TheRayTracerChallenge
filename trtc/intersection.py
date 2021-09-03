

class Intersection():
    def __init__(self, t, object) -> None:
        self.t = t
        self.object = object

class IntersectionList():
    def __init__(self, *argv) -> None:
        self.count = len(argv)
        self.intersections = [a for a in argv]