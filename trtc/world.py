import math
from .light import PointLight
from .tuple import Tuple, color, point
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

    def shade_hit(self, comps, remaining=4):
        '''
        Return the color at the intersection encapsulated by pomps in the given world
        '''
        shadowed = self.is_shadowed(comps.over_point)
        surface = comps.object.material.lighting(
            comps.object, self.light, comps.over_point, comps.eyev, comps.normalv, shadowed)
        reflected = self.reflected_color(comps)
        refracted = self.refracted_color(comps, remaining)

        material = comps.object.material
        if material.reflective > 0 and material.transparency > 0:
            reflectance = comps.schlick()
            return surface + reflected * reflectance + refracted * (1 - reflectance)
            
        return surface + reflected + refracted

    def color_at(self, ray, remaining=4):
        '''
        Intersect the world with the given ray and then return the color at the 
        resulting intersection.
        '''
        xs = self.intersect_world(ray)
        hit = xs.hit()
        if hit is None:
            return color(0, 0, 0)
        comps = hit.prepare_computations(ray)
        return self.shade_hit(comps)

    def is_shadowed(self, p):
        '''
        Check to see if point p is in a shadow
        '''
        v = self.light.position - p
        distance = v.magnitude()
        direction = v.normalize()

        r = Ray(p, direction)
        intersections = self.intersect_world(r)

        h = intersections.hit()
        if h and h.t < distance:
            return True
        return False

    def reflected_color(self, comps, remaining=4):
        if remaining < 1:
            return color(0, 0, 0)
        if comps.object.material.reflective == 0.0:
            return color(0, 0, 0)

        reflect_ray = Ray(comps.over_point, comps.reflectv)
        reflect_color = self.color_at(reflect_ray, remaining-1)

        return reflect_color * comps.object.material.reflective

    def refracted_color(self, comps, remaining):
        '''
        If the surface is opaque (comps.object.material.transparency = 0) or 
        we've reached the max number of recursions (remaining = 0) or
        total internal refraction > 1
        return black
        '''
        if comps.object.material.transparency == 0 or remaining == 0:
            return color(0, 0, 0)

        # Calculate total internal refraction
        n_ratio = comps.n1 / comps.n2
        cos_i = comps.eyev.dot(comps.normalv)
        sin2_t = n_ratio**2 * (1 - cos_i**2)
        if sin2_t > 1:
            return color(0, 0, 0)

        cos_t = math.sqrt(1.0 - sin2_t)
        direction = comps.normalv * \
            (n_ratio * cos_i - cos_t) - comps.eyev * n_ratio
        refract_ray = Ray(comps.under_point, direction)
        refract_ray_color = self.color_at(
            refract_ray, remaining-1) * comps.object.material.transparency
        return refract_ray_color
