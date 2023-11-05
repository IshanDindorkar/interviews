"""
Single Linked List implementation and associated operations
"""
from interviews.custom_exceptions.invalid_operation import InvalidOperation
from interviews.udemy_examples.linked_list.sll_node import SLLNode


class SingleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._num_nodes = 0

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node: SLLNode):
        self._head = node

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node: SLLNode):
        self._tail = node

    def append(self, node: SLLNode):
        # Check if the list is empty => head and tail pointers should point to None
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            last_node = self._tail
            self._tail = node
            last_node.next = node

        self._num_nodes += 1

    def prepend(self, node: SLLNode):
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            first_node = self._head
            self._head = node
            node.next = first_node

        self._num_nodes += 1

    def insert(self, index: int, node: SLLNode):
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

    def get(self, index: int):
        if index == -1:
            return self._tail
        elif index <= self._num_nodes:
            current_node = self._head
            for _ in range(index):
                current_node = current_node.next

            return current_node
        else:
            raise IndexError("Invalid index")

    def set(self, index: int, value: int):
        node = self.get(index=index)
        node.value = value

    def reverse(self):
        prev_node = None
        current_node = self._head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self._head, self._tail = self._tail, self._head

    def pop(self):
        # Check for an empty LL
        if self._head is None:
            raise InvalidOperation("Popping element from an empty Linked List!")
        else:
            current_node = self._head
            for _ in range(1, self._num_nodes - 1):
                current_node = current_node.next

            self._tail = current_node
            current_node.next = None
            self._num_nodes -= 1

    def pop_first(self):
        if self._head is None:
            raise InvalidOperation("Popping element from an empty Linked List!")
        else:
            first_node = self._head
            self._head = first_node.next
            first_node.next = None
            self._num_nodes -= 1

    def remove_by_index(self, index: int):
        if self._head is None:
            raise InvalidOperation("Removing element from an empty Linked List!")
        else:
            node = self.get(index=index - 1)
            node_to_be_removed = node.next
            node.next = node_to_be_removed.next
            node_to_be_removed.next = None
            self._num_nodes -= 1

    def remove_by_value(self, value: int):
        if self._head is None:
            raise InvalidOperation("Removing element from an empty Linked List!")
        else:
            self._num_nodes -= 1
            current_node = self._head
            # Edge case: If the value to be deleted is the first element of LL
            if current_node.value == value:
                self._head = current_node.next
                current_node.next = None
            else:
                for index in range(1, self._num_nodes - 1):
                    current_node = self.get(index)
                    prev_node = self.get(index - 1)
                    if current_node is not None and current_node.value == value:
                        prev_node.next = current_node.next

    def remove_duplicates(self):
        unique_elements = set()

        current_node = self._head
        unique_elements.add(current_node.value)
        while current_node.next is not None:
            if current_node.next.value in unique_elements:
                current_node.next = current_node.next.next
                self._num_nodes -= 1
            else:
                unique_elements.add(current_node.next.value)
                current_node = current_node.next

    def delete_all(self):
        self._head = None
        self._tail = None

    def __str__(self):
        sll_rep = ""
        current_node = self._head
        while current_node is not None:
            sll_rep += str(current_node.value) + " "
            current_node = current_node.next

        return sll_rep.strip()


def main():
    # Step 1: Creation of new nodes
    node_1 = SLLNode(value=1)
    node_2 = SLLNode(value=5)
    node_3 = SLLNode(value=15)
    node_4 = SLLNode(value=20)
    node_5 = SLLNode(value=12)

    # Step 2.1: Creating new Single Linked List
    single_linked_list = SingleLinkedList()
    single_linked_list.append(node_2)
    single_linked_list.append(node_3)
    single_linked_list.append(node_4)
    print(f"Initialized Single Linked List: \n{single_linked_list}")

    # Step 2.2: Prepend new node element after Linked List is created
    single_linked_list.prepend(node_1)
    print(f"Post prepending element: \n{single_linked_list}")

    # Step 3: Inserting a new node in the middle of LL
    single_linked_list.insert(index=2, node=node_5)
    # single_linked_list.insert(index=0, node=node_5)  # edge case!
    print(f"After inserting node with value {node_5.value} at index 2: \n{single_linked_list}")

    # Step 4: Search an element in the LL
    value = 15
    # value = 50  # negative test!
    print(f"The index of value {value} is {single_linked_list.search(value=value)}")

    # Step 5: Get last element in the LL
    node = single_linked_list.get(index=-1)
    print(f"The last element is {node.value}")

    # Step 6: Replace element "5" with "6"
    single_linked_list.set(index=1, value=6)
    print(f"Replacing element 5 with 6: \n{single_linked_list}")

    # Step 7: Removing last element
    single_linked_list.pop()
    print(f"After removing last element: \n{single_linked_list}")
    single_linked_list.append(node=node_4)

    # Step 8: Removing first element from LL
    single_linked_list.pop_first()
    print(f"After removing first element: \n{single_linked_list}")
    single_linked_list.prepend(node_1)

    # Step 9: Removing element from index 3
    single_linked_list.remove_by_index(index=3)
    print(f"After removing element at index 3: \n{single_linked_list}")
    single_linked_list.insert(index=3, node=node_3)

    # Step 10: Reverse LL
    single_linked_list.reverse()
    print(f"After reversing: \n {single_linked_list}")
    single_linked_list.reverse()

    # Step 11: Removing duplicates from LL
    node_6 = SLLNode(value=15)
    node_7 = SLLNode(value=20)
    node_8 = SLLNode(value=12)
    single_linked_list.append(node_6)
    single_linked_list.append(node_7)
    single_linked_list.append(node_8)
    print(f"Added duplicates: {single_linked_list}")

    single_linked_list.remove_duplicates()
    print(f"After removing duplicates: {single_linked_list}")

    # Step 12: Removing element 15 from LL
    # single_linked_list.remove_by_value(value=15)
    # print(f"After removing element 15: {single_linked_list}")

    # Step 12: Removing element 1 from LL
    single_linked_list.remove_by_value(value=1)
    print(f"After removing element 1: {single_linked_list}")


if __name__ == "__main__":
    main()

# EOF
