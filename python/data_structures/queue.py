from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        new_addition = Node(value)
        if self.back:
            self.back.next = new_addition
        self.back = new_addition
        if not self.front:
            self.front = self.back

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError("Queue Empty, Try Again Later")
        old_front = self.front
        self.front = old_front.next
        return old_front.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError("Queue Empty, Try Again Later")
        return self.front.value

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False
