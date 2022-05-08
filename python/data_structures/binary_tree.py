class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self):
        def traverse(root, values):
            if not root:
                return
            values.append(root.value)
            traverse(root.left, values)
            traverse(root.right, values)
        values = []
        traverse(self.root, values)
        return values

    def in_order(self):
        def traverse(root, values):
            if not root:
                return
            traverse(root.left, values)
            values.append(root.value)
            traverse(root.right, values)
        values = []
        traverse(self.root, values)
        return values

    def post_order(self):
        def traverse(root, values):
            if not root:
                return
            traverse(root.left, values)
            traverse(root.right, values)
            values.append(root.value)
        values = []
        traverse(self.root, values)
        return values


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
