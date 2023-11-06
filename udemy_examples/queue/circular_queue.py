"""
Circular Queue implementation
"""
from interviews.custom_exceptions.invalid_operation import InvalidOperation


class CircularQueue:
    def __init__(self, max_size=0):
        self._items = [None] * max_size
        self._start = -1
        self._top = -1
        self._max_size = max_size

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start: int):
        self._start = start

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, top: int):
        self._top = top

    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, max_size: int):
        self._max_size = max_size

    @property
    def items(self):
        return self._items

    def is_full(self):
        if self.start == 0 and self.top + 1 == self.max_size:
            # this is condition where a queue is ideally considered as
            # full as the start ptr is at 0 index and the top ptr will
            # reach the max size of queue
            return True
        elif self.top + 1 == self.start:
            # this happens when top ptr is just below the start ptr
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def enqueue(self, value: int):
        if self.is_full():
            raise InvalidOperation("Queue is full, enqueue operation rejected!")

        if self.top == self.max_size:
            # to prevent top ptr from overflowing, we reset it to 0
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:  # imp to check if we are enqueuing first element
                self.start += 1
        self.items[self.top] = value

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperation("Queue is empty, dequeue operation rejected!")

        first_element = self.items[self.start]
        start_ptr = self.start
        if self.start == self.max_size:
            # again to prevent overflowing of start ptr, we reset it to 0
            self.start = 0
        else:
            self.start += 1
            if self.start == self.top:
                self.top = -1   # queue is empty now
                self.start = -1
        self.items[start_ptr] = None

        return first_element


def main():
    circular_queue = CircularQueue(max_size=5)
    circular_queue.enqueue(1)
    circular_queue.enqueue(2)
    circular_queue.enqueue(3)
    circular_queue.enqueue(4)
    circular_queue.enqueue(5)
    print(f"Circular Queue after enqueuing multiple elements: \n {circular_queue.items}")

    circular_queue.dequeue()
    circular_queue.dequeue()
    print(f"Circular Queue after dequeuing multiple elements: \n {circular_queue.items}")


if __name__ == "__main__":
    main()

# EOF
