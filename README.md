# RoboNav

A 2D robot navigation simulator written in Python. The robot plans the shortest path across a grid containing obstacles using the **A\* (A-star) algorithm**, then follows that path step by step. The result is drawn with matplotlib.

Built for the **Applied Robotics and AI Project (Assignment 1)**, BEng Robotics and AI, University of Hertfordshire.

## What it does

1. Builds a 10x10 grid map with walls (obstacles).
2. Uses A* to find the shortest route from a start cell to a goal cell.
3. Moves a simulated robot along that route, recording its trail.
4. Plots the obstacles, the path, the start (green circle) and the goal (red star).

## How A* works (short version)

A* explores the grid starting from the start cell. For every cell it scores:

    f = g + h

- **g** is the number of steps taken from the start to this cell.
- **h** is a heuristic estimate of the distance from this cell to the goal.

The cell with the lowest `f` is explored next, so the search heads towards the goal instead of wandering. When the goal is reached, the path is rebuilt by following the "came from" links backwards. If the goal cannot be reached, the planner returns `None`.

The heuristic depends on the movement mode:

| Movement mode | Heuristic used |
|---|---|
| 4 directions (up, down, left, right) | Manhattan distance |
| 8 directions (diagonals allowed) | Chebyshev distance |

In this project every move, including a diagonal one, costs 1 step.

## Results

On the demo map (start at `(0, 0)`, goal at `(9, 9)`):

| Mode | Steps taken |
|---|---|
| 4-direction movement | 18 |
| 8-direction (diagonal) movement | 13 |

Diagonal movement was added on the `feature/diagonal-moves` branch and then merged into `main`.

## Requirements

- Python 3.9 or newer
- matplotlib (listed in `requirements.txt`)

## Installation

```bash
git clone https://github.com/dharshanthehacker-arch/robonav.git
cd robonav
pip install -r requirements.txt
```

## Usage

Run the simulation. A window opens showing the map and the planned path:

```bash
python3 -m src.main
```

Run the unit tests:

```bash
python3 -m unittest discover -s tests -t .
```

To change the map, edit `build_grid()` in `src/main.py`. To switch between 4 and 8 direction movement, change `diagonal=True` to `diagonal=False` in the same function.

## Project structure

    robonav/
      README.md             Project overview (this file)
      requirements.txt      Python dependencies
      .gitignore            Files Git should not track
      src/
        grid.py             Grid map, obstacles and neighbour lookup
        robot.py            Robot position and movement along a path
        planner.py          A* path planning algorithm
        main.py             Builds the map, runs the planner, plots the result
      tests/
        test_planner.py     Unit tests for the planner
      docs/
        add-commit-push.md  Explanation of git add, commit and push

## Tests

The unit tests check that the planner:

- finds a straight path on an empty grid,
- goes around an obstacle,
- returns `None` when the goal is walled off.

## Git workflow used in this project

This repository was built with small, focused commits, each made with `git add`, `git commit` and `git push`. A separate branch, `feature/diagonal-moves`, was used to develop diagonal movement before merging it into `main`. The repository was also cloned into a fresh folder to confirm it works from scratch.

See [docs/add-commit-push.md](docs/add-commit-push.md) for a written explanation of the three core commands and how they differ.

## Author

bobby, BEng Robotics and AI, University of Hertfordshire.
