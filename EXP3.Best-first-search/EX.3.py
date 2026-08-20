import heapq

# Graph: node -> neighboring nodes
graph = {
    'A': ['B', 'C', 'D'],
    'B': [],
    'C': ['E', 'F'],
    'D': ['H'],
    'E': [],
    'F': ['I', 'G'],
    'G': [],
    'H': [],
    'I': []
}

# Heuristic values h(n)
heuristic = {
    'A': 15,
    'B': 13,
    'C': 10,
    'D': 14,
    'E': 11,
    'F': 8,
    'G': 0,
    'H': 9,
    'I': 4
}


def best_first_search(start, goal):
    # Priority queue: (heuristic value, node)
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))

    visited = set()
    parent = {start: None}

    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        print("Expanded:", current, "h =", h)

        # Goal found
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        # Add neighboring nodes
        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    return None


# Start Best-First Search
path = best_first_search('A', 'G')

print("\nPath:", " -> ".join(path))