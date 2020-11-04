class Ant:
    def __init__(self):
        # 0 - front
        # 1 - right
        # 2 - back
        # 3 - left
        self.direction = 0

    def change_direction(self, dir):
        self.direction += dir

        if self.direction < 0:
            self.direction = 3
        if self.direction > 3:
            self.direction = 0
