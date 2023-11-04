class Node:
    def __init__(self, value: int):
        self._value = value
        self._next = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

# EOF
