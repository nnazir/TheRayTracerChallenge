from trtc import color


class Material():
    def __init__(self) -> None:
        self.color = color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0

    def __eq__(self, o: object) -> bool:
        return self.color == o.color and \
            self.ambient == o.ambient and \
            self.diffuse == o.diffuse and \
            self.specular == o.specular and \
            self.shininess == o.shininess
