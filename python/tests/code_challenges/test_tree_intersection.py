import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection

# @pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)

def test_additional_value():
    tree_a = BinaryTree()
    values = [1,2,3,4,5,6]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = [7,8,9,10,5,3,2]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a,tree_b)
    expected = [5,3,2]

    assert sorted(actual) == sorted(expected)

def test_non_numerical_values():
    tree_a = BinaryTree()
    values = ['abab','cdcd','efef','ghgh','ijoj','klkl','mnmn','opop',]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = ['qrqr','stst','uvuv', 'wxwx','yzyz', 'abab','efef']
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a,tree_b)
    expected = ['abab','efef']

    assert sorted(actual) == sorted(expected)


def test_booleans():
    tree_a = BinaryTree()
    values = [True]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = [True, False]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [True]

    assert sorted(actual) == sorted(expected)

# @pytest.mark.skip("TODO")
def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)
