class Grid:
    """A 2D grid map where some cells are obstacles."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_free(self, x, y):
        return self.in_bounds(x, y) and (x, y) not in self.obstacles

    def neighbors(self, x, y):
        """Return free cells reachable in 4 directions."""
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if self.is_free(nx, ny):
                result.append((nx, ny))
        return result

    def __str__(self):
        rows = []
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += "#" if (x, y) in self.obstacles else "."
            rows.append(row)
        return "\n".join(rows)
