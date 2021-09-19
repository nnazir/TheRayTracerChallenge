

class Intersection():
    def __init__(self, t, object) -> None:
        self.t = t
        self.object = object

    def __lt__(self, other):
        return self.t < other.t


class IntersectionList():
    def __init__(self, *argv) -> None:
        self.count = len(argv)
        self.intersections = [a for a in argv]
        self.intersections.sort()

    def add(self, item):
        self.intersections.append(item)
        self.count = len(self.intersections)

    def sort_intersections(self):
        list.sort(self.intersections, key=lambda i: i.t)

    def hit(self):
        '''
        Assumes the list of intersections are sorted. Returns the lowest positive intersection.
        '''
        for i in self.intersections:
            if i.t > 0:
                return i
