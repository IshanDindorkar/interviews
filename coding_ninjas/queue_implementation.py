"""
DS: Queue implementation (FIFO: First in, First Out)
"""
from typing import List

from loguru import logger

from interviews.custom_exceptions.invalid_operation import InvalidOperation


class Queue:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items: List):
        self._items = items

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, element):
        self._items.append(element)

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperation("Cannot remove element from empty queue")
        else:
            self._items.pop(0)    # remove element from the front of queue

    def peek(self):
        return self._items[0]


def main():
    bank_teller_queue = Queue()

    # Initializing queue with persons
    queue_elements = ["Person 1", "Person 2", "Person 3"]
    bank_teller_queue.items = queue_elements

    # Adding new person to the queue using operation "enqueue"
    bank_teller_queue.enqueue("Person 4")
    logger.info(f"Queue looks like this: {bank_teller_queue.items}")

    # Check who is at the front of the queue
    front_elem = bank_teller_queue.peek()
    logger.info(f"Front person in the queue is: {front_elem}")

    # Serviced front person and now he is removed using operation "dequeue"
    bank_teller_queue.dequeue()
    front_elem = bank_teller_queue.peek()
    logger.info(f"Now the front person in the queue is: {front_elem}")


if __name__ == "__main__":
    main()

# EOF
