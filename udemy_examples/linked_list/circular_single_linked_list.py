"""
Circular Single Linked List operations
"""

from interviews.custom_exceptions.invalid_operation import InvalidOperation
from interviews.udemy_examples.linked_list.sll_node import SLLNode
from interviews.udemy_examples.linked_list.single_linked_list import SingleLinkedList


class CircularSingleLinkedList(SingleLinkedList):  # CSLL for short
    def append(self, new_node: SLLNode):
        if self.head is None:
            # CSLL is empty
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            last_node = self.tail
            last_node.next = new_node
            self.tail = new_node

            new_node.next = self.head  # last node pointing back to first node

        self._num_nodes += 1

    def prepend(self, new_node: SLLNode):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            last_node = self.tail
            last_node.next = new_node

        self._num_nodes += 1

    def insert(self, index: int, new_node: SLLNode):
        # Edge case: when CSLL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node

        # If index = 0, it is prepend operation
        if index == 0:
            self.prepend(new_node=new_node)
        elif index > self._num_nodes:
            # this is append operation
            self.append(new_node=new_node)
        else:
            current_node = self.head
            for _ in range(0, index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

        self._num_nodes += 1

    def search(self, value: int):
        if self.head is None:
            raise InvalidOperation("Circular Single Linked List is empty!")

        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

        return None

    def get(self, index: int):
        if self.head is None:
            raise InvalidOperation("Circular Single Linked List is empty!")

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def set(self, index: int, value: int):
        node = self.get(index=index)
        node.value = value

    def pop(self):
        if self.head is None:
            raise InvalidOperation("CSLL is empty, hence no pop operation can be done!")

        last_node = self.tail
        prev_node = self.head
        while prev_node is not None:
            if prev_node.next == last_node:
                break
            prev_node = prev_node.next

        self.tail = prev_node
        prev_node.next = self.head

        last_node.next = None
        self._num_nodes -= 1

    def pop_first(self):
        if self.head is None:
            raise InvalidOperation("CSLL is empty, hence no pop operation can be done!")

        first_node = self.head
        self.head = first_node.next
        last_node = self.tail
        last_node.next = self.head

        self._num_nodes -= 1

    def remove_by_index(self, index: int):
        if index > self._num_nodes:
            raise InvalidOperation("Index value is more than number of nodes in the CSLL!")

        if index == 0:
            self.pop_first()
        elif index == self._num_nodes - 1:
            self.pop()
        else:
            node_to_be_deleted = self.get(index=index)
            prev_node = self.get(index=index - 1)
            prev_node.next = node_to_be_deleted.next
            node_to_be_deleted.next = None

        self._num_nodes -= 1

    def remove_by_value(self, value: int):
        if self.head is None:
            raise InvalidOperation("CSLL is empty!")

        node_to_be_deleted = self.search(value=value)  # search node with given value
        prev_node = self.head
        while prev_node is not None:
            if prev_node.next == node_to_be_deleted:
                prev_node.next = node_to_be_deleted.next  # de-reference node to be deleted
                break
            prev_node = prev_node.next

        node_to_be_deleted.next = None
        self._num_nodes -= 1

    def __str__(self):
        current_node = self.head
        csll_rep = ""

        while current_node is not None:
            csll_rep += str(current_node.value) + " "
            current_node = current_node.next

            if current_node == self.head:  # Exit condition to break out of loop
                break

        return (csll_rep.strip().replace(" ", " -> ")
                + " -> " + str(current_node.value))  # last part to show that it is a circular linked list


def main():
    # Step 1: Creating new nodes
    node_1 = SLLNode(value=1)
    node_2 = SLLNode(value=2)
    node_3 = SLLNode(value=3)
    node_4 = SLLNode(value=4)
    node_5 = SLLNode(value=5)
    node_6 = SLLNode(value=6)

    # Step 2: Building circular single linked list
    csll = CircularSingleLinkedList()
    csll.append(new_node=node_1)
    csll.append(new_node=node_2)
    csll.append(new_node=node_3)
    csll.append(new_node=node_4)
    csll.append(new_node=node_5)
    csll.append(new_node=node_6)
    print(f"Circular Single Linked List: \n{csll}")

    # Step 4: Prepending element to CSLL
    node_0 = SLLNode(value=0)
    csll.prepend(new_node=node_0)
    print(f"New CSLL after prepending: \n{csll}")

    # Step 5: Inserting element at different positions in the CSLL
    node_34 = SLLNode(value=34)
    csll.insert(index=4, new_node=node_34)
    print(f"CSLL after inserting at index 4: \n{csll}")

    node_7 = SLLNode(value=7)
    csll.insert(index=8, new_node=node_7)
    print(f"CSLL after inserting at index 8: \n{csll}")

    node_neg_1 = SLLNode(value=-1)
    csll.insert(index=0, new_node=node_neg_1)
    print(f"CSLL after inserting at index 0: \n{csll}")

    # Step 6: Get element at index #4
    expected_index = 4
    orig_value = csll.get(index=expected_index).value
    print(f"The element at index {expected_index} is {csll.get(index=expected_index).value}")

    # Step 6: Modify element at index #4
    expected_index = 4
    new_value = -3
    csll.set(index=expected_index, value=new_value)
    print(f"CSLL after modifying value at {expected_index} with new value {new_value}: \n{csll}")
    csll.set(index=expected_index, value=orig_value)

    # Step 7: Remove element based on index
    index_of_node_to_deleted = 0
    csll.remove_by_index(index=index_of_node_to_deleted)
    print(f"CSLL after removing node at index {index_of_node_to_deleted}: \n{csll}")

    index_of_node_to_deleted = 4
    csll.remove_by_index(index=index_of_node_to_deleted)
    print(f"CSLL after removing node at index {index_of_node_to_deleted}: \n{csll}")

    index_of_node_to_deleted = 6
    csll.remove_by_index(index=index_of_node_to_deleted)
    print(f"CSLL after removing node at index {index_of_node_to_deleted}: \n{csll}")
    csll.insert(index=index_of_node_to_deleted, new_node=node_6)

    # Step 7: Remove element based on value
    value_of_node_to_deleted = 3
    csll.remove_by_value(value=value_of_node_to_deleted)
    print(f"CSLL after removing node with value {value_of_node_to_deleted}: \n{csll}")
    csll.insert(index=3, new_node=node_3)


if __name__ == "__main__":
    main()

# EOF
