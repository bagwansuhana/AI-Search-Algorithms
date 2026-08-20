# Best First Search

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['T'],
    'F': ['R'],
    'G': ['N'],
    'H': ['O', 'P'],
    'I': ['Q'],
    'J': ['R']
}

# Heuristic values
h = {
    'A': 10,
    'B': 4,
    'C': 4,
    'D': 6,
    'E': 5,
    'F': 5,
    'G': 4,
    'H': 3,
    'I': 4,
    'J': 4,
    'N': 0,
    'O': 2,
    'P': 3,
    'Q': 0,
    'R': 4,
    'T': 5
}


def best_first_search(start, goal):

    open_list = [start]
    visited = []

    while open_list:

        # Select node with smallest heuristic
        current = open_list[0]

        for node in open_list:
            if h[node] < h[current]:
                current = node

        open_list.remove(current)
        visited.append(current)

        print("Visiting:", current)

        # Goal test
        if current == goal:
            print("\nGoal found!")
            print("Traversal:", " -> ".join(visited))
            return

        # Add children
        for child in graph.get(current, []):
            if child not in visited and child not in open_list:
                open_list.append(child)

    print("Goal not found")


# Start and goal
best_first_search('A', 'O')