"""
Binary Tree implementation:

1. Pre-order traversal
2. In-order traversal
3. Post-order traversal
4. Level-order traversal
5. Search an element
6. Insertion of new element
7. Deletion of an element

Time complexity for all cases: O(n)
Space complexity for all cases: O(n)
"""
import queue

from interviews.udemy_examples.tree.binary_tree_node import BinaryTreeNode


class BinaryTree:
    def __init__(self, root_node):
        self._root_node = root_node

    def pre_order_traversal(self, root_node: BinaryTreeNode):
        # Base condition
        if root_node is None:
            return

        # Step 1: Visit root node
        print(root_node.data)

        # Step 2: Traverse left subtree
        self.pre_order_traversal(root_node=root_node.left_child)

        # Step 3: Traverse right subtree
        self.pre_order_traversal(root_node=root_node.right_child)

    def in_order_traversal(self, root_node: BinaryTreeNode):
        # Base condition
        if root_node is None:
            return

        # Step 1: Visit left subtree
        self.in_order_traversal(root_node=root_node.left_child)

        # Step 2: Visit root node
        print(root_node.data)

        # Step 3: Visit right subtree
        self.in_order_traversal(root_node=root_node.right_child)

    def post_order_traversal(self, root_node: BinaryTreeNode):
        # Base condition
        if root_node is None:
            return

        # Step 1: Visit left subtree
        self.post_order_traversal(root_node=root_node.left_child)

        # Step 2: Visit right subtree
        self.post_order_traversal(root_node=root_node.right_child)

        # Step 3: Visit root node
        print(root_node.data)

    def level_order_traversal(self, root_node: BinaryTreeNode):
        if root_node is None:  # Base condition
            return

        tracking_queue = queue.Queue()
        tracking_queue.put(root_node)
        while not tracking_queue.empty():
            first_node = tracking_queue.get()
            print(first_node.data)

            if first_node.left_child is not None:
                tracking_queue.put(first_node.left_child)
            if first_node.right_child is not None:
                tracking_queue.put(first_node.right_child)

    def search(self, root_node: BinaryTreeNode, element):
        if root_node is None:  # Base condition
            return

        tracking_queue = queue.Queue()
        tracking_queue.put(root_node)
        while not tracking_queue.empty():
            first_node = tracking_queue.get()
            if first_node.data == element:
                return f"{element} found in the list of beverages"

            if first_node.left_child is not None:
                tracking_queue.put(first_node.left_child)
            if first_node.right_child is not None:
                tracking_queue.put(first_node.right_child)

        return f"{element} not found in the list of beverages"

    def insert(self, root_node: BinaryTreeNode, element):
        new_node = BinaryTreeNode(data=element)

        # If tree is empty, make new element as root node
        if root_node is None:
            root_node = new_node

        # Tree is not empty, find the first node having empty left or right child
        tracking_queue = queue.Queue()
        tracking_queue.put(root_node)
        while not tracking_queue.empty():
            first_node = tracking_queue.get()

            if first_node.left_child is None:
                first_node.left_child = new_node
                break
            else:
                tracking_queue.put(first_node.left_child)

            if first_node.right_child is None:
                first_node.right_child = new_node
                break
            else:
                tracking_queue.put(first_node.right_child)

    def delete(self, root_node: BinaryTreeNode, element):
        if root_node is None:
            return

        tracking_queue = queue.Queue()
        tracking_queue.put(root_node)
        while not tracking_queue.empty():
            first_node = tracking_queue.get()
            if first_node.data == element:
                # Three-step process
                # 1. Find the deepest node i.e. node not having left and right child
                # 2. Set the node to be deleted as the deepest node value
                # 3. Remove deepest node from BT
                deepest_node = self._get_deepest_node(root_node=first_node)
                first_node.data = deepest_node.data
                self._remove_deepest_node(root_node=first_node, deepest_node=deepest_node)

            if first_node.left_child is not None:
                tracking_queue.put(first_node.left_child)
            if first_node.right_child is not None:
                tracking_queue.put(first_node.right_child)

    #######################################################
    ##########          Helper Methods            #########
    #######################################################
    def _get_deepest_node(self, root_node: BinaryTreeNode):
        if root_node is None:
            return

        tracking_queue = queue.Queue()
        tracking_queue.put(root_node)
        first_node = None
        while not tracking_queue.empty():
            first_node = tracking_queue.get()
            if first_node.left_child is not None:
                tracking_queue.put(first_node.left_child)
            if first_node.right_child is not None:
                tracking_queue.put(first_node.right_child)

        return first_node

    def _remove_deepest_node(self, root_node: BinaryTreeNode, deepest_node: BinaryTreeNode):
        if root_node is None:
            return

        tracking_queue = queue.Queue()
        tracking_queue.put(root_node)
        while not tracking_queue.empty():
            first_node = tracking_queue.get()
            if first_node.left_child == deepest_node:
                first_node.left_child = None
                break
            else:
                tracking_queue.put(first_node.left_child)
            if first_node.right_child == deepest_node:
                first_node.right_child = None
                break
            else:
                tracking_queue.put(first_node.right_child)


def main():
    beverage = BinaryTreeNode(data="Drinks")
    hot_beverage = BinaryTreeNode(data="Hot")
    cold_beverage = BinaryTreeNode(data="Cold")

    beverage.left_child = hot_beverage
    beverage.right_child = cold_beverage

    binary_tree = BinaryTree(root_node=beverage)

    print("\nPre-order traversal =>")
    binary_tree.pre_order_traversal(root_node=beverage)

    print("\nIn-order traversal =>")
    binary_tree.in_order_traversal(root_node=beverage)

    print("\nPost-order traversal =>")
    binary_tree.post_order_traversal(root_node=beverage)

    print("\nLevel-order traversal =>")
    tea = BinaryTreeNode(data="Tea")
    coffee = BinaryTreeNode(data="Coffee")
    coke = BinaryTreeNode(data="Coke")
    sprite = BinaryTreeNode(data="Sprite")
    hot_beverage.left_child = tea
    hot_beverage.right_child = coffee
    cold_beverage.left_child = coke
    cold_beverage.right_child = sprite

    binary_tree.level_order_traversal(root_node=beverage)

    print("\nSearch an element in the Binary Tree =>")
    print(binary_tree.search(root_node=beverage, element="Tea"))
    print(binary_tree.search(root_node=beverage, element="Fanta"))  # Negative test

    print("\nInserting new element in Binary Tree")
    binary_tree.insert(root_node=beverage, element="Green Tea")
    binary_tree.level_order_traversal(root_node=beverage)

    print("\nDeleting node from Binary Tree")
    binary_tree.delete(root_node=beverage, element="Tea")
    binary_tree.level_order_traversal(root_node=beverage)


if __name__ == "__main__":
    main()

# EOF

