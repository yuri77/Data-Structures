from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # insersion and deletion is very fast for head and tail operation. queue is FIFO structure which works well with head tail pointer system of DLL

        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size = self.storage.length

    def dequeue(self):
        if self.size > 0:
            value = self.storage.remove_from_head()
            self.size = self.storage.length
            return value
        else:
            return

    def len(self):
        return self.size
