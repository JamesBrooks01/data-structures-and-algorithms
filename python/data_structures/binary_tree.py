from data_structures.queue import Queue


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

    def add(self,value):
        node = Node(value)
        if not self.root:
            self.root = node
            return
        breadth = Queue()
        breadth.enqueue(self.root)
        while not breadth.is_empty():
            front = breadth.dequeue()
            if not front.left:
                front.left = node
                return
            else:
                breadth.enqueue(front.left)
            if not front.right:
                front.right = node
                return
            else:
                breadth.enqueue(front.right)
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
