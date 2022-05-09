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

    def find_maximum_value(self):
        def traverse(root, value):
            if not root:
                return
            if root.value > value[0]:
                value.pop()
                value.append(root.value)
            traverse(root.left, value)
            traverse(root.right, value)
        final_value = [0]
        traverse(self.root, final_value)
        return int(final_value[0])

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
