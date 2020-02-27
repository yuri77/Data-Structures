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
        self.storage.remove_from_head()
        self.size = self.storage.length

    def len(self):
        return self.size
