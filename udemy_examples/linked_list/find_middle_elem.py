from interviews.udemy_examples.linked_list.sll_node import SLLNode
from interviews.udemy_examples.linked_list.single_linked_list import SingleLinkedList


def find_middle_element(head: SLLNode):
    fast = head
    while fast and fast.next:
        head = head.next
        fast = fast.next.next

    return head


def main():
    # Creating individual nodes
    node_1 = SLLNode(value=5)
    node_2 = SLLNode(value=1)
    node_3 = SLLNode(value=46)
    node_4 = SLLNode(value=89)
    node_5 = SLLNode(value=34)
    node_6 = SLLNode(value=55)

    # Adding nodes to LL
    single_linked_list = SingleLinkedList()
    single_linked_list.append(node=node_1)
    single_linked_list.append(node=node_2)
    single_linked_list.append(node=node_3)
    single_linked_list.append(node=node_4)
    single_linked_list.append(node=node_5)
    single_linked_list.append(node=node_6)
    print(f"Single Linked List: \n{single_linked_list}")

    # Finding node in the middle of LL
    middle_node = find_middle_element(head=single_linked_list.head)
    print(f"Middle element: {middle_node.value}")


if __name__ == "__main__":
    main()

# EOF
