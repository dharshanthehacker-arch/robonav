class Robot:
    """A simulated robot that follows a list of grid cells."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.trail = [(x, y)]

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.trail.append((x, y))

    def follow_path(self, path):
        """Move through each cell of a path, skipping the starting cell."""
        for x, y in path[1:]:
            self.move_to(x, y)

    @property
    def position(self):
        return (self.x, self.y)
