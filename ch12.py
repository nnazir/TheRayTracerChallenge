import math
from trtc.utils import save_canvas
from trtc.tuple import color, point, vector
from trtc.matrix import Matrix
from trtc.sphere import Sphere
from trtc.plane import Plane
from trtc.material import Material
from trtc.world import World
from trtc.light import PointLight
from trtc.camera import Camera
from trtc.pattern import CheckersPattern
from trtc.cube import Cube
import datetime

starttime = datetime.datetime.now()

world = World()
cube = Cube()
sphere = Sphere()

world.light = PointLight(point(-10, 10, -10), color(1, 1, 1))



wall = Plane()
wall.transform = Matrix.translation(0, 0, 15) * Matrix.rotation_x(math.pi/2)
wall.material.color = color(1, 1, 1)
wall.material.reflective = 0.0

floor = Plane()
floor.transform = Matrix.translation(0, -1, 0)
floor.material.reflective = 1.0
floor.material.transparency = 1.0
floor.material.refractive_index = 1.5
floor.material.specular = 0
floor.material.pattern = CheckersPattern(color(1, 0, 0), color(1, 1, 1))

cube.transform = Matrix.scaling(1, 1, 0.5) * Matrix.translation(-2, 0, 0)
cube.material.color = color(0.83, 0.20, 0.21)
cube.material.specular = 0.5

sphere.transform = Matrix.scaling(
    0.5, 0.5, 0.5) * Matrix.translation(0.5, 1, 1)
sphere.material.color = color(0.73, 0.76, 0.80)
sphere.material.diffuse = 0.7
sphere.material.specular = 5
sphere.material.shininess = 300
sphere.material.transparency = 0
sphere.material.reflective = 0.5

world.objects.append(wall)
world.objects.append(cube)
world.objects.append(sphere)
world.objects.append(floor)


camera = Camera(1024, 768, math.pi/3)
camera.transform = Matrix.view_transform(
    point(0, 1.5, -5), point(0, 1, 0), vector(0.75, 1, 0))

print("Rendering world")
renderstarttime = datetime.datetime.now()
canvas = camera.render(world)
print(f"Time to render: {datetime.datetime.now() - renderstarttime}")

print("Saving canvas")

save_canvas("output/ch12-7.ppm", canvas)
endtime = datetime.datetime.now()
print(f"Run time: {endtime-starttime}")
