from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front_of_queue = None
        self.back_of_queue = None

    def enqueue(self, value):
        new_addition = Node(value)
        if self.back_of_queue:
            self.back_of_queue.next = new_addition
        self.back_of_queue = new_addition
        if not self.front_of_queue:
            self.front_of_queue = self.back_of_queue

    def dequeue(self):
        if not self.front_of_queue:
            raise InvalidOperationError("Queue Empty, Try Again Later")
        old_front_of_queue = self.front_of_queue
        self.front_of_queue = old_front_of_queue.next
        return old_front_of_queue.value

    def peek(self):
        if not self.front_of_queue:
            raise InvalidOperationError("Queue Empty, Try Again Later")
        return self.front_of_queue.value

    def IsEmpty(self):
        if self.front_of_queue == None:
            return True
        else:
            return False
