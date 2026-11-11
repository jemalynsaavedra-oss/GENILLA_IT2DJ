class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return

    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    print("Binary Tree BFS:", " -> ".join(result))


def dfs_preorder(root):
    result = []

    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    print("Binary Tree DFS:", " -> ".join(result))


if __name__ == "__main__":
    root = TreeNode("G")
    root.left = TreeNode("E")
    root.right = TreeNode("N")
    root.left.left = TreeNode("I")
    root.left.right = TreeNode("L")
    root.right.left = TreeNode("L")
    root.right.right = TreeNode("A")

    bfs(root)
    dfs_preorder(root)