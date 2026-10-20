import matplotlib.pyplot as plt

from src.grid import Grid
from src.planner import astar
from src.robot import Robot


def build_grid():
    grid = Grid(10, 10)
    for y in range(1, 8):
        grid.add_obstacle(4, y)
    for x in range(6, 9):
        grid.add_obstacle(x, 5)
    return grid


def show(grid, robot, start, goal):
    fig, ax = plt.subplots(figsize=(6, 6))
    for ox, oy in grid.obstacles:
        ax.add_patch(plt.Rectangle((ox, oy), 1, 1, color="black"))
    xs = [x + 0.5 for x, _ in robot.trail]
    ys = [y + 0.5 for _, y in robot.trail]
    ax.plot(xs, ys, "b-o", markersize=4, label="Path")
    ax.plot(start[0] + 0.5, start[1] + 0.5, "go", markersize=12, label="Start")
    ax.plot(goal[0] + 0.5, goal[1] + 0.5, "r*", markersize=15, label="Goal")
    ax.set_xlim(0, grid.width)
    ax.set_ylim(0, grid.height)
    ax.set_aspect("equal")
    ax.invert_yaxis()
    ax.grid(True)
    ax.legend(loc="upper right")
    ax.set_title("RoboNav: A* path planning")
    plt.show()


def main():
    grid = build_grid()
    start, goal = (0, 0), (9, 9)
    path = astar(grid, start, goal)
    if path is None:
        print("No path found.")
        return
    robot = Robot(*start)
    robot.follow_path(path)
    print(f"Path found in {len(path) - 1} steps.")
    show(grid, robot, start, goal)


if __name__ == "__main__":
    main()
