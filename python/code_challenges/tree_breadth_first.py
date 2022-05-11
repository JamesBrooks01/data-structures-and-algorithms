from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    output_list = []
    if not tree or not tree.root:
        return output_list
    breadth = Queue()
    breadth.enqueue(tree.root)
    while not breadth.is_empty():
        front = breadth.dequeue()
        output_list.append(front.value)
        if front.left is not None:
            breadth.enqueue(front.left)
        if front.right is not None:
            breadth.enqueue(front.right)
    return output_list
