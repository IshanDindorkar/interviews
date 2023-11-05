"""
Stack implementation using Single Linked List
"""
from interviews.custom_exceptions.invalid_operation import InvalidOperation
from interviews.udemy_examples.linked_list.dll_node import DLLNode


class Stack:
    def __init__(self):
        self._top = None
        self._num_nodes = 0

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, top: DLLNode):
        self._top = top

    def push(self, new_node: DLLNode):
        if self.top is None:
            self.top = new_node
        else:
            top_node = self.top
            top_node.next = new_node
            new_node.prev = top_node
            self.top = new_node

        self._num_nodes += 1

    def pop(self):
        if self.top is None:
            raise InvalidOperation("Stack is empty, pop operation rejected!")
        else:
            top_node = self.top
            popped_node = top_node
            prev_node = top_node.prev
            self.top = prev_node
            prev_node.next = None

            # De-referencing top node to send it for GC
            top_node.prev = None
            top_node.next = None

            return popped_node

    def peek(self):
        if self.top is None:
            raise InvalidOperation("Stack is empty, peek operation rejected!")
        else:
            top_node = self.top

            return top_node

    def __str__(self):
        stack_elements = []

        current_node = self.top
        while current_node is not None:
            stack_elements.append(current_node.value)
            current_node = current_node.prev
        stack_elements.reverse()
        stack_elements = [str(elem) for elem in stack_elements]

        return " -> ".join(stack_elements)


def main():
    # Step 1: Create independent nodes to be stacked
    node_1 = DLLNode(value=1)
    node_2 = DLLNode(value=2)
    node_3 = DLLNode(value=3)
    node_4 = DLLNode(value=4)
    node_5 = DLLNode(value=5)

    # Step 2: Create stack of nodes such that the last one added is on the top
    stack = Stack()
    stack.push(new_node=node_1)
    stack.push(new_node=node_2)
    stack.push(new_node=node_3)
    stack.push(new_node=node_4)
    stack.push(new_node=node_5)
    print(f"Stack elements: \n{stack}")

    # Step 3: Popping top node from stack
    popped_node = stack.pop()
    print(f"Popped node: \n{popped_node.value}")
    print(f"Stack after popping: \n{stack}")

    top_node = stack.peek()
    print(f"Top element now in the stack: \n{top_node.value}")


if __name__ == "__main__":
    main()

# EOF
