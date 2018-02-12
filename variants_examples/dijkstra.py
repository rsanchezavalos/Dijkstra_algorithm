from collections import defaultdict
from heapq import *


def dijkstra_shortest_path(edges, start, end):
    """
    Function that receives a list of distance between edges
    and calculates the shortest path
    """

    # Create a dictionary of distances between two edges.
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    # Create object to store the results.
    q, seen = [(0, start, ())], set()

    while q:
        # keep every path and save the current state
        # Pop and return the smallest item from the heap
        (cost, v1, path) = heappop(q)

        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == end:
                return (cost, path)

            # Get all possible roads from the current node
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))

    return float("inf")


if __name__ == "__main__":
    edges = [
        ("A", "B", 12),
        ("A", "D", 30),
        ("B", "C", 10),
        ("B", "D", 800),
        ("B", "E", 40),
        ("C", "E", 20),
        ("D", "E", 15),
        ("D", "F", 60),
        ("E", "F", 85),
        ("E", "G", 90),
        ("F", "G", 100)
    ]

