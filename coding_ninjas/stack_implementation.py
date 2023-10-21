"""
DS: Stack implementation (LIFO: Last In, First Out)
"""

from loguru import logger

from interviews.custom_exceptions.invalid_operation import InvalidOperation


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, element):
        self._items.append(element)

    def pop(self):
        if self.is_empty():
            raise InvalidOperation("Removing element from empty stack")
        else:
            logger.info(f"Popping last element: {self._items[-1]}")
            self._items.pop()

    def peek(self):
        return self._items[-1]


def main():
    kitchen_stack = Stack()

    # Pushing elements to stack
    kitchen_stack.push("Plate 1")
    kitchen_stack.push("Plate 2")
    kitchen_stack.push("Plate 3")

    # Peeking at the last most element in the stack
    last_elem = kitchen_stack.peek()
    logger.info(f"Last most element in the stack: {last_elem}")

    # Pop out the last element
    kitchen_stack.pop()
    last_elem = kitchen_stack.peek()
    logger.info(f"Last most element in the stack: {last_elem}")

    for cnt in range(3):
        kitchen_stack.pop()
        kitchen_stack.pop()
        kitchen_stack.pop()


if __name__ == "__main__":
    main()

# EOF
