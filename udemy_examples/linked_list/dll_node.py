"""
Definition of Node class used for creation of Double Linked List
"""

from interviews.udemy_examples.linked_list.sll_node import SLLNode


class DLLNode(SLLNode):
    def __init__(self, value):
        super().__init__(value=value)
        self._prev = None

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node):
        self._prev = node

# EOF
