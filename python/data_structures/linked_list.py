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
        newNode = Node(value, self.head)
        self.head = newNode

    def concat_list(self):
        list_item = self.head
        linked_list_string = ""
        while list_item is not None:
            linked_list_string += f"{{ {list_item.value} }} -> "
            list_item = list_item.next
        return linked_list_string

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        current = self.head
        while current is not None:
            if current.next == None:
                newNode = Node(value, None)
                current.next = newNode
                break
            current = current.next

    def insert_before(self, value, new_value):
        if not self.head or not self.includes(value):
            raise TargetError
        current = self.head
        priorNode = None
        while current is not None:
            if current.value == value:
                newNode = Node(new_value, current)
                if priorNode == None:
                    self.head = newNode
                else:
                    priorNode.next = newNode
                break
            priorNode = current
            current = current.next

    def insert_after(self, value, new_value):
        if not self.includes(value):
            raise TargetError
        current = self.head
        while current is not None:
            if current.value == value:
                newNode = Node(new_value, current.next)
                current.next = newNode
                break
            current = current.next


class Node:
    def __init__(data_node, data, next):
        data_node.value = data
        data_node.next = next


class TargetError(BaseException):
    pass
