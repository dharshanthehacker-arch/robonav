import heapq


def heuristic(a, b):
    """Manhattan distance between two cells."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    """Find the shortest path from start to goal using A*.

    Returns a list of (x, y) cells, or None if no path exists.
    """
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for neighbor in grid.neighbors(*current):
            new_g = g_score[current] + 1
            if neighbor not in g_score or new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                f = new_g + heuristic(neighbor, goal)
                came_from[neighbor] = current
                heapq.heappush(open_set, (f, neighbor))

    return None
