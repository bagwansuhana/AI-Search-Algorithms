# Best First Search

import heapq

# Graph with heuristic values
graph = {
    'S': [('A', 7), ('B', 2), ('C', 3)],
    'A': [('B', 3), ('D', 4)],
    'B': [('D', 4), ('H', 1)],
    'C': [('L', 2)],
    'D': [('F', 5)],
    'H': [('F', 3), ('G', 2)],
    'L': [('I', 4), ('J', 4)],
    'I': [('K', 4)],
    'J': [('K', 4)],
    'G': [('F', 2)],
    'K': [('F', 5)],
    'F': []
}

# Heuristic values shown inside the nodes
heuristic = {
    'S': 10,
    'A': 9,
    'B': 7,
    'C': 8,
    'D': 8,
    'H': 6,
    'F': 6,
    'G': 3,
    'L': 6,
    'I': 4,
    'J': 4,
    'K': 3
}


def best_first_search(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))

    visited = set()
    parent = {start: None}

    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        print("Visiting:", current, "Heuristic:", h)

        if current == goal:
            break

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                if neighbor not in parent:
                    parent[neighbor] = current

                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    # Construct path
    if goal not in visited:
        print("Goal not found")
        return

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("\nBest First Search Path:")
    print(" -> ".join(path))


# Run the algorithm
best_first_search('S', 'F')