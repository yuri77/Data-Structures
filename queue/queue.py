"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!

linked list approach is faster with O(1). It can access the head right away
   Array pop method takes O(n) when the first element is taken out from the array, underlying index needs to be re-indexed and shifted. 
   Linked list approach is faster in Queue 
"""
from singly_linked_list import LinkedList
from stack import Stack

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(0)
#         else:
#             return None


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.add_to_tail(value)

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.remove_head()
#         else:
#             return None

class Queue:
    def __init__(self):
        self.size = 0
        self.first_stack = Stack()
        self.second_stack = Stack()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.first_stack.push(value)

    def dequeue(self):
        if self.size == 0:
            return None

        self.size -= 1
        if self.second_stack.size == 0:
            while self.first_stack.size:
                value = self.first_stack.pop()
                self.second_stack.push(value)
            return self.second_stack.pop()
        if self.second_stack.size > 0:
            return self.second_stack.pop()
