from random import randint

from interviews.udemy_examples.linked_list.dll_node import DLLNode
from interviews.udemy_examples.linked_list.double_linked_list import DoubleLinkedList


def add(dll: DoubleLinkedList, new_node: DLLNode):
    if dll.head is None:
        dll.head = new_node
        dll.tail = new_node
    else:
        last_node = dll.tail
        last_node.next = new_node
        new_node.prev = last_node
        dll.tail = new_node


def generate_random_linked_list(dll: DoubleLinkedList,
                                num: int,
                                min: int,
                                max: int):
    for _ in range(num):
        new_node = DLLNode(value=randint(a=min, b=max))
        add(dll=dll, new_node=new_node)


def print_dll(dll: DoubleLinkedList):
    dll_rep = ""

    current_node = dll.head
    while current_node is not None:
        dll_rep += str(current_node.value) + " "
        current_node = current_node.next

    print(dll_rep.strip(" ").replace(" ", " -> "))


def main():
    double_linked_list = DoubleLinkedList()
    length = int(input("How many numbers in the Linked List? \n"))
    min_range = 0
    max_range = 100

    generate_random_linked_list(dll=double_linked_list,
                                num=length,
                                min=min_range,
                                max=max_range)

    print_dll(dll=double_linked_list)


if __name__ == "__main__":
    main()

# EOF
