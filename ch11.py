import math
import datetime
from trtc.utils import save_canvas
from trtc.tuple import point, vector, color
from trtc.matrix import Matrix
from trtc.world import World
from trtc.ray import Ray
from trtc.plane import Plane
from trtc.sphere import Sphere
from trtc.light import PointLight
from trtc.camera import Camera
from trtc.pattern import CheckersPattern

starttime = datetime.datetime.now()
world = World()
# world.default_world()
r = Ray(point(0, 0, -3), vector(0, -math.sqrt(2)/2, math.sqrt(2)/2))
floor = Plane()
floor.transform = Matrix.translation(0, -1, 0)
floor.material.reflective = 1.0
floor.material.transparency = 1.0
floor.material.refractive_index = 1.5
floor.material.specular = 0
floor.material.pattern = CheckersPattern(color(1, 0, 0), color(1, 1, 1))
ball = Sphere()
ball.material.color = color(1, 0, 0)
ball.material.ambient = 0.5
ball.material.diffuse = 0.5
ball.material.specular = 0.2
ball.material.transparency = 0.9
ball.material.reflective = 0.9
ball.transform = Matrix.scaling(1, 1, 1) * Matrix.translation(2, 4, 6)
world.objects.append(floor)
world.objects.append(ball)

world.light = PointLight(point(10, 10, -10), color(1, 1, 1))

camera = Camera(800, 600, math.pi/3)

camera.transform = Matrix.view_transform(point(0, 1.5, -5),
                                         point(0, 1, 0),
                                         vector(0, 1, 0))

print("Rendering world")
renderstarttime = datetime.datetime.now()
canvas = camera.render(world)
print(f"Time to render: {datetime.datetime.now() - renderstarttime}")

print("Saving canvas")
savestarttime = datetime.datetime.now()
save_canvas("output/ch11-5.ppm", canvas)
print(f"Time to save to canvas: {datetime.datetime.now() - savestarttime}")

endtime = datetime.datetime.now()
print(f"Run time: {endtime-starttime}")
