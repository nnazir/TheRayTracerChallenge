from trtc import color
from math import pow


class Material():
    def __init__(self) -> None:
        self.color = color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0
        self.pattern = None

    def __eq__(self, o: object) -> bool:
        return self.color == o.color and \
            self.ambient == o.ambient and \
            self.diffuse == o.diffuse and \
            self.specular == o.specular and \
            self.shininess == o.shininess

    def lighting(self, obj, light, position, eyev, normalv, in_shadow=False):
        if self.pattern:
            lighting_color = self.pattern.stripe_at_object(obj, position)
        else:
            lighting_color = self.color

        # combine the surface color with the light's color/intensity
        effective_color = lighting_color * light.intensity

        # find the direction to the light source
        lightv = (light.position - position).normalize()

        # compute the ambient contribution
        ambient = effective_color * self.ambient

        if in_shadow:
            return ambient
        else:
            # light_dot_normal represents the cosine of the angle between the
            # light vector and the normal vector. A negative number means the
            # light is on the other side of the surface.
            light_dot_normal = lightv.dot(normalv)
            if light_dot_normal < 0:
                diffuse = color(0, 0, 0)
                specular = color(0, 0, 0)
            else:
                # compute the diffuse contribution
                diffuse = effective_color * self.diffuse * light_dot_normal
                # reflect_dot_eye represents the cosine of the angle between the
                # reflection vector and the eye vector. A negative number means the
                # light reflects away from the eye.
                reflectv = -lightv.reflect(normalv)
                reflect_dot_eye = reflectv.dot(eyev)
                if reflect_dot_eye <= 0:
                    specular = color(0, 0, 0)
                else:
                    # compute the specular contribution
                    factor = pow(reflect_dot_eye, self.shininess)
                    specular = light.intensity * self.specular * factor

            # Add the three contributions together to get the final shading
            return ambient + diffuse + specular
