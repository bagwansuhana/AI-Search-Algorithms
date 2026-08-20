# DFS (Depth First Search) program

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def dfs(root):
    if root is None:
        return

    # Visit root
    print(root.data, end=" ")

    # Visit left subtree
    dfs(root.left)

    # Visit right subtree
    dfs(root.right)


# Creating the tree

root = Node(5)

root.left = Node(3)
root.right = Node(7)

root.left.left = Node(2)
root.left.right = Node(4)

root.right.right = Node(8)

root.left.right.right = Node(8)


# DFS traversal
print("DFS Traversal:")
dfs(root)