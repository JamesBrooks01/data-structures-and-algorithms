class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        return_string = self.concat_list()
        if self.head == None:
            return "NULL"
        return f"{return_string}NULL"

    def insert(self, value):
        # method body here
        newNode = Node()
        newNode.value = value
        newNode.ref = self.head
        self.head = newNode

    def concat_list(self):
        list_item = self.head
        linked_list_string = ""
        while list_item is not None:
            linked_list_string += f"{{ {list_item.value} }} -> "
            list_item = list_item.ref
        return linked_list_string

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.ref
        return False

class Node:
    def __init__(data_node, data = None):
        data_node.value = data
        data_node.ref = "NULL"


class TargetError:
    pass
