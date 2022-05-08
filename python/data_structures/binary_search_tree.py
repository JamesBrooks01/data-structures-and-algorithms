from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def add(self, value):
        def traverse(root, new_node):
            if not root:
                return
            if new_node.value < root.value:
                if root.left:
                    traverse(root.left, new_node)
                else:
                    root.left = new_node
            else:
                if root.right:
                    traverse(root.right, new_node)
                else:
                    root.right = new_node

        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        traverse(self.root, new_node)

    def contains(self, value):
        def traverse(root, value):
            if not root:
                return
            if value < root.value:
                if root.left:
                    if root.left.value == value:
                        return True
                    else:
                        traverse(root.left, value)
                else:
                    return False
            else:
                if root.right:
                    if root.right.value == value:
                        return True
                    else:
                        traverse(root.right, value)
                else:
                    return False
        answer = traverse(self.root, value)
        if answer == True:
            return answer
        else:
            return False
