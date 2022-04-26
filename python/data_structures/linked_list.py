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
            print("List Item", list_item.value)
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

    def append(self, value):
        current = self.head
        while current is not None:
            if current.ref == None:
                newNode = Node()
                newNode.value = value
                newNode.ref = None
                current.ref = newNode
                break
            current = current.ref

    def insert_before(self, value, new_value):
        if not self.head or not self.includes(value):
            raise TargetError
        current = self.head
        priorNode = None
        while current is not None:
            if current.value == value:
                newNode = Node()
                newNode.value = new_value
                newNode.ref = current
                if priorNode == None:
                    self.head = newNode
                else:
                    priorNode.ref = newNode
                break
            priorNode = current
            current = current.ref

    def insert_after(self, value, new_value):
        if not self.includes(value):
            raise TargetError
        current = self.head
        while current is not None:
            if current.value == value:
                newNode = Node()
                newNode.value = new_value
                newNode.ref = current.ref
                current.ref = newNode
                break
            current = current.ref


class Node:
    def __init__(data_node, data = None):
        data_node.value = data
        data_node.ref = "NULL"


class TargetError(BaseException):
    pass
