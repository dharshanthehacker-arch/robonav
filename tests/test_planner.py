import unittest

from src.grid import Grid
from src.planner import astar


class TestPlanner(unittest.TestCase):
    def test_straight_path(self):
        g = Grid(5, 5)
        path = astar(g, (0, 0), (4, 0))
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (4, 0))
        self.assertEqual(len(path), 5)

    def test_avoids_obstacle(self):
        g = Grid(5, 5)
        g.add_obstacle(2, 0)
        path = astar(g, (0, 0), (4, 0))
        self.assertNotIn((2, 0), path)
        self.assertEqual(path[-1], (4, 0))

    def test_no_path(self):
        g = Grid(3, 3)
        for y in range(3):
            g.add_obstacle(1, y)
        self.assertIsNone(astar(g, (0, 0), (2, 2)))


if __name__ == "__main__":
    unittest.main()
