from .light import PointLight
from .tuple import color, point
from .sphere import Sphere
from .matrix import Matrix
from .ray import Ray
from .intersection import IntersectionList


class World():
    def __init__(self) -> None:
        self.objects = []
        self.light = None

    def __contains__(self, item):
        for i in self.objects:
            if i.material == item.material and \
                    i.transform == item.transform:
                return True
        return False

    def default_world(self):
        ''' Generates a default world to work with a light source
        at (-10, 10, -10) and two concentric spheres. One sphere is a 
        unit sphere and the innermost sphere has a radius of 0.5. '''
        self.light = PointLight(point(-10, 10, -10), color(1, 1, 1))
        s1 = Sphere()
        s1.material.color = color(0.8, 1.0, 0.6)
        s1.material.diffuse = 0.7
        s1.material.specular = 0.2
        s2 = Sphere()
        s2.transform = Matrix.scaling(0.5, 0.5, 0.5)
        self.objects = [s1, s2]

    def intersect_world(self, ray):
        ''' Iterate over all of the objects that have been added to 
        the world, intersecting each of them with the ray, and 
        aggregating the intersections into a single collection.

        Returns sorted intersections of rays with a world '''

        xs = IntersectionList()
        for i in self.objects:
            for j in i.intersect(ray).intersections:
                xs.add(j)

        xs.sort_intersections()
        return xs

    def shade_hit(self, comps):
        '''
        Return the color at the intersection encapsulated by pomps in the given world
        '''
        return comps.object.material.lighting(self.light, comps.point, comps.eyev, comps.normalv)
