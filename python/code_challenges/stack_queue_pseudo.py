from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, value):
        self.inbox.push(value)

    def dequeue(self):
        outbox_result = self.outbox.is_empty()
        inbox_result = self.inbox.is_empty()
        if outbox_result:
            while inbox_result == False:
                in_value = self.inbox.pop()
                self.outbox.push(in_value)
                inbox_result = self.inbox.is_empty()

        return self.outbox.pop()
