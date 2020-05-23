class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head:
            self.head = self.tail = new_node

        else:
            # in order to add to tail, we need to find the current tail by
            # traversing the list
            # current = self.head
            # while(current):
            #     current = current.next
            # current.next = new_node
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        if not self.head:
            return None

        else:
            self.length -= 1
            prev = None
            current = self.head
            while(current.next):
                prev = current
                current = current.next
            if prev is None:
                self.head = None
            else:
                prev.next = None
            return current.value

    def contains(self, value):
        if not self.head:
            return None
        else:
            current = self.head
            current_value = current.value
            while(current):
                if current.value == value:
                    return True
                current = current.next
            return False

    def remove_head(self):
        if not self.head:
            return None

        if self.head == self.tail:
            self.length -= 1
            current_head_value = self.head.value
            self.head = self.tail = None
            return current_head_value

        else:
            self.length -= 1
            current_head = self.head
            self.head = self.head.next
            current_head.next = None
            return current_head.value

    def get_max(self):
        if not self.head:
            return None
        else:
            maximum = self.head.value
            current = self.head
            while(current):
                if current.value > maximum:
                    maximum = current.value
                current = current.next
            return maximum
