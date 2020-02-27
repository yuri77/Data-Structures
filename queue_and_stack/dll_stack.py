from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? LIFO
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size = self.storage.length

    def pop(self):
        if self.size > 0:
            value = self.storage.remove_from_head()
            self.size = self.storage.length
            return value
        else:
            return

    def len(self):
        return self.size
