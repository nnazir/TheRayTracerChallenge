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

floor = Plane()
# floor.transform = Matrix.scaling(15, 0.05, 15)
# floor.transform = Matrix.scaling(
#     10, 0.01, 10) * Matrix.translation(1, 1, 1)
floor.material = Material()
floor.material.color = color(1, 0.9, 0.9)
floor.material.specular = 0
floor.material.pattern = CheckersPattern(color(1, 0, 0), color(1, 1, 1))

world = World()
world.light = PointLight(point(-10, 20, -10), color(1, 1, 1))
world.objects.append(floor)

camera = Camera(800, 600, math.pi/2)
camera.transform = Matrix.view_transform(point(0, 2.0, -15),
                                         point(0, 2, 0),
                                         vector(0, 1, 0))

canvas = camera.render(world)
save_canvas("output/ch10-4.ppm", canvas)
