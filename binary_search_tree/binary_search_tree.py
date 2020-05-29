"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # compare to the root node, if smaller insert to left
        # otherwise insert to right
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # end case when target is equal to the value
        if target == self.value:
            return True
        else:
            # case if target is smaller than current node
            if target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            # case when target is larger than current node
            else:
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        # check right side only because right side contains nodes that are larger in value
        # end case-> if there is no right side, then current node is the largest value
        if not self.right:
            return max_value
        else:
            return self.right.get_max()

    # def iterative_get_max(self):
    #     max_value = self.value
    #     current = self

    #     while current:
    #         if current.value > max_value:
    #             max_value = current.value
    #         current = current.right
    #     return max_value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    '''
    Depth First Traversals:
    -Inorder (left,root,right)
    -preorder (root,left,right)
    -postorder (left,right,root) 
    '''

    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            node_current = q.dequeue()
            print(node_current.value)
            if node_current.left:
                q.enqueue(node_current.left)
            if node_current.right:
                q.enqueue(node_current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        st = Stack()
        st.push(self)
        while st.size > 0:
            node_current = st.pop()
            print(node_current.value)
            if node_current.left:
                st.push(node_current.left)
            if node_current.right:
                st.push(node_current.right)

        # make a stack
        # push the node on the stack
        # while the stack is not empty
        # pop off the stack, this is our curent node
        # put the kids on the stack

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self.left)
        if self.right:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(node)
        if self.right:
            self.right.post_order_dft(node)
        print(self.value)
