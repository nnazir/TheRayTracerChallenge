from trtc.utils import float_equal


class Matrix():
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def __eq__(self, o: object) -> bool:
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                if not float_equal(self.matrix[row][col], o.matrix[row][col]):
                    return False
        return True
