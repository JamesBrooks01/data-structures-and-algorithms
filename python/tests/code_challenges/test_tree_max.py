import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

def test_max_val_larger_tree():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(51)
    tree.root.right = Node(364)
    tree.root.left.left = Node(45637)
    tree.root.left.right = Node(2134)
    tree.root.right.left = Node(753)
    tree.root.right.right = Node(64)

    actual = tree.find_maximum_value()
    expected = 45637
    assert actual == expected

def test_max_val_example():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.right.right = Node(9)
    tree.root.left.right = Node(6)
    tree.root.right.right.left = Node(4)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)

    actual = tree.find_maximum_value()
    expected = 11
    assert actual == expected
