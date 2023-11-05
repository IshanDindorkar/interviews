"""
Merge two sorted Single Linked Lists
"""
from interviews.udemy_examples.linked_list.sll_node import SLLNode
from interviews.udemy_examples.linked_list.single_linked_list import SingleLinkedList


def merge_sorted_lists(list_1: SingleLinkedList, list_2: SingleLinkedList):
    merged_list_node = SLLNode(value=-1)

    prev = merged_list_node  # Pointer for the merged list
    current_node_l1 = list_1.head
    current_node_l2 = list_2.head
    while current_node_l1 is not None and current_node_l2 is not None:
        if current_node_l1.value <= current_node_l2.value:
            prev.next = current_node_l1
            current_node_l1 = current_node_l1.next
        else:
            prev.next = current_node_l2
            current_node_l2 = current_node_l2
        prev = prev.next

    if current_node_l1 is not None:
        prev.next = current_node_l1
    else:
        prev.next = current_node_l2

    return merged_list_node.next


def print_merged_list(merged_list_node: SLLNode):
    merged_list = ""
    current_node = merged_list_node
    while current_node is not None:
        merged_list += str(current_node.value) + " "
        current_node = current_node.next

    print(f"Merged list: {merged_list.strip()}")


def main():
    node_1 = SLLNode(value=1)
    node_2 = SLLNode(value=2)
    node_3 = SLLNode(value=3)
    node_4 = SLLNode(value=4)
    node_5 = SLLNode(value=5)
    node_6 = SLLNode(value=6)

    list_1 = SingleLinkedList()
    list_1.append(node_1)
    list_1.append(node_2)
    list_1.append(node_3)
    print(f"List 1: {list_1}")

    list_2 = SingleLinkedList()
    list_2.append(node_4)
    list_2.append(node_5)
    list_2.append(node_6)
    print(f"List 2: {list_2}")

    merge_list_node = merge_sorted_lists(list_1=list_1, list_2=list_2)
    print_merged_list(merged_list_node=merge_list_node)


if __name__ == "__main__":
    main()

# EOF

