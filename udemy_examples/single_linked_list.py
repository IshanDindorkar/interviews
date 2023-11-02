"""
Single Linked List implementation and associated operations
"""


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


class SingleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._num_nodes = 0

    def append(self, node: Node):
        # Check if the list is empty => head and tail pointers should point to None
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            last_node = self._tail
            self._tail = node
            last_node.next = node

        self._num_nodes += 1

    def prepend(self, node: Node):
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            first_node = self._head
            self._head = node
            node.next = first_node

        self._num_nodes += 1

    def insert(self, index: int, node: Node):
        if self._head is None:
            self._head = node
            self._tail = node
        elif index > 0:
            current_node = self._head
            for _ in range(index - 1):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
        else:
            self.prepend(node=node)

        self._num_nodes += 1

    def search(self, value: int):
        current_node = self._head

        index = 0
        while current_node is not None:
            if current_node.value == value:
                return index
            index += 1
            current_node = current_node.next

        return -1

    def __str__(self):
        sll_rep = ""
        current_node = self._head
        while current_node is not None:
            sll_rep += str(current_node.value) + " "
            current_node = current_node.next

        return sll_rep.strip()


def main():
    # Step 1: Creation of new nodes
    node_1 = Node(value=1)
    node_2 = Node(value=5)
    node_3 = Node(value=15)
    node_4 = Node(value=20)
    node_5 = Node(value=12)

    # Step 2.1: Creating new Single Linked List
    single_linked_list = SingleLinkedList()
    single_linked_list.append(node_2)
    single_linked_list.append(node_3)
    single_linked_list.append(node_4)

    # Step 2.2: Prepend new node element after
    # Linked List is created
    single_linked_list.prepend(node_1)

    # Step 3: Inserting a new node in the middle of LL
    single_linked_list.insert(index=2, node=node_5)
    # single_linked_list.insert(index=0, node=node_5)  # edge case!

    # Step 4: Search an element in the LL
    value = 15
    # value = 50  # negative test!
    print(f"The index of value {value} is {single_linked_list.search(value=value)}")

    # Step 5: Printing out the Single Linked List
    print(single_linked_list)


if __name__ == "__main__":
    main()

# EOF
