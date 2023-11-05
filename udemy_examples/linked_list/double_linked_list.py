"""
Double Linked List operations
"""
from interviews.custom_exceptions.invalid_operation import InvalidOperation
from interviews.udemy_examples.linked_list.dll_node import DLLNode
from interviews.udemy_examples.linked_list.single_linked_list import SingleLinkedList


class DoubleLinkedList(SingleLinkedList):
    def __init__(self):
        super().__init__()

    def append(self, new_node: DLLNode):
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            last_node = self._tail
            last_node.next = new_node
            new_node.prev = last_node
            self._tail = new_node

        self._num_nodes += 1

    def prepend(self, new_node: DLLNode):
        if self._head is None:
            self._head = new_node
        else:
            first_node = self._head
            new_node.next = first_node
            first_node.prev = new_node
            self._head = new_node

        self._num_nodes += 1

    def insert(self, index: int, new_node: DLLNode):
        if self._head is None:
            self._head = new_node
            self._tail = new_node

        if index == 0:
            # Inserting new node at the beginning of DLL
            self.prepend(new_node=new_node)
        elif index >= self._num_nodes:
            # Inserting new node at the end of DLL
            self.append(new_node=new_node)
        else:
            current_node = self._head
            for _ in range(index):
                current_node = current_node.next
            prev_node = current_node.prev

            # Establishing prev and next links for new node
            new_node.next = current_node
            new_node.prev = prev_node

            # Hooking up new node in between prev and current nodes
            current_node.prev = new_node
            prev_node.next = new_node

        self._num_nodes += 1

    def pop(self):
        if self.head is None:
            raise InvalidOperation("DLL is empty, pop operation rejected!")

        last_node = self.tail
        prev_node = last_node.prev
        prev_node.next = None

        last_node.prev = None
        last_node.next = None  # should be None but just setting it to be safe

        self.tail = prev_node
        self._num_nodes -= 1

    def pop_first(self):
        if self.head is None:
            raise InvalidOperation("DLL is empty, pop first operation rejected!")

        first_node = self.head
        next_node = first_node.next
        next_node.prev = None
        first_node.next = None

        self.head = next_node
        self._num_nodes -= 1

    def remove_by_index(self, index: int):
        if self.head is None:
            raise InvalidOperation("DLL is empty, pop first operation rejected!")

        if index > self._num_nodes:
            raise IndexError("Invalid index value")

        if index == 0:
            self.pop_first()
        elif index == self._num_nodes - 1:
            self.pop()
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next

            prev_node = current_node.prev
            next_node = current_node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            current_node.prev = None
            current_node.next = None

            self._num_nodes -= 1

    def __str__(self):
        dll_rep = ""

        current_node = self.head
        while current_node is not None:
            dll_rep += str(current_node.value) + " "
            current_node = current_node.next

        return dll_rep.strip().replace(" ", " <-> ")

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next


def main():
    # Step 1: Create independent nodes
    node_1 = DLLNode(value=1)
    node_2 = DLLNode(value=2)
    node_3 = DLLNode(value=3)
    node_4 = DLLNode(value=4)
    node_5 = DLLNode(value=5)
    node_6 = DLLNode(value=6)
    node_7 = DLLNode(value=7)

    # Step 2: Append nodes to DLL
    dll = DoubleLinkedList()
    dll.append(new_node=node_1)
    dll.append(new_node=node_2)
    dll.append(new_node=node_3)
    dll.append(new_node=node_4)
    dll.append(new_node=node_5)
    dll.append(new_node=node_6)
    dll.append(new_node=node_7)

    dll_elems = [node.value for node in dll]
    print(f"Double Linked List elements: \n{dll_elems}")
    print(f"Double Linked List as string representation: \n{dll}")

    # Step 3: Prepend new node to DLL
    node_0 = DLLNode(value=0)
    dll.prepend(new_node=node_0)
    print(f"DLL after prepending a new node: \n{dll}")

    # Step 4: Insert new nodes at different positions in DLL
    node_45 = DLLNode(value=45)
    dll.insert(index=5, new_node=node_45)
    print(f"DLL after inserting a new node: \n{dll}")

    node_neg_1 = DLLNode(value=-1)
    dll.insert(index=0, new_node=node_neg_1)
    print(f"DLL after inserting a new node: \n{dll}")

    # Step 5: Removing nodes from different indices
    dll.remove_by_index(index=0)
    print(f"DLL after removing node from index 0: \n{dll}")

    dll.remove_by_index(index=5)
    print(f"DLL after removing node from index 5: \n{dll}")


if __name__ == "__main__":
    main()

# EOF
