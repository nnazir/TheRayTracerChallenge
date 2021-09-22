from trtc.utils import save_canvas
from trtc.tuple import color, point, vector
from trtc.matrix import Matrix
from trtc.sphere import Sphere
from trtc.material import Material
from trtc.world import World
from trtc.light import PointLight
from trtc.camera import Camera
from math import pi

floor = Sphere()
floor.transform = Matrix.scaling(10, 0.01, 10)
floor.material = Material()
floor.material.color = color(1, 0.9, 0.9)
floor.material.specular = 0

left_wall = Sphere()
left_wall.transform = Matrix.translation(
    0, 0, 5) * Matrix.rotation_y(-pi/4) * Matrix.rotation_x(pi/2) * Matrix.scaling(10, 0.01, 10)
left_wall.material = floor.material

right_wall = Sphere()
right_wall.transform = Matrix.translation(
    0, 0, 5) * Matrix.rotation_y(pi/4) * Matrix.rotation_x(pi/2) * Matrix.scaling(10, 0.01, 10)
right_wall.material = floor.material

middle = Sphere()
middle.transform = Matrix.translation(-0.5, 1, 0.5)
middle.material = Material()
middle.material.color = color(0.1, 1, 0.5)
middle.material.diffuse = 0.7
middle.material.specular = 0.3

right = Sphere()
right.transform = Matrix.translation(
    1.5, 0.5, -0.5) * Matrix.scaling(0.5, 0.5, 0.5)
right.material = Material()
right.material.color = color(0.5, 1, 0.1)
right.material.diffuse = 0.7
right.material.specular = 0.3

left = Sphere()
left.transform = Matrix.translation(-1.5, 0.33, -0.75) * \
    Matrix.scaling(0.33, 0.33, 0.33)
left.material = Material()
left.material.color = color(1, 0.8, 0.1)
left.material.diffuse = 0.7
left.material.specular = 0.3

world = World()
world.light = PointLight(point(-10, 10, -10), color(1, 1, 1))

world.objects.append(floor)
world.objects.append(left_wall)
world.objects.append(right_wall)
world.objects.append(middle)
world.objects.append(right)
world.objects.append(left)

camera = Camera(800, 600, pi/3)
camera.transform = Matrix.view_transform(point(0, 1.5, -5),
                                         point(0, 1, 0),
                                         vector(0, 1, 0))

canvas = camera.render(world)
save_canvas("output/ch7-2.ppm", canvas)
