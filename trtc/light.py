from trtc import point


class PointLight():
    def __init__(self, position, intensity) -> None:
        self.position = position
        self.intensity = intensity

    def __eq__(self, o: object) -> bool:
        return self.position == o.position and \
            self.intensity == o.intensity
