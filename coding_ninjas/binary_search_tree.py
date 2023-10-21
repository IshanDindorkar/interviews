"""
Binary Search Tree implementation
"""


class Node:
    def __init__(self, key):
        self._value = key
        self._left = None
        self._right = None

    @property
    def key(self):
        return self._value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def insert(self, key):
        self._root = self._insert_recursive(self._root, key)

    def search(self, key):
        return self._search_recursive(self._root, key)

    def _insert_recursive(self, root: Node, key: int):
        if root is None:
            return Node(key=key)
        elif key < root.key:
            root.left = self._insert_recursive(root=root.left, key=key)
        else:
            root.right = self._insert_recursive(root=root.right, key=key)

        return root

    def _search_recursive(self, root: Node, key: int):
        if root is None or key == root.key:
            return root
        if key < root.key:
            return self._search_recursive(root=root.left, key=key)
        else:
            return self._search_recursive(root=root.right, key=key)


def main():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(34)
    bst.insert(55)
    bst.insert(5)
    bst.insert(89)
    bst.insert(3)

    if bst.search(55):
        print("Target found in the tree")


if __name__ == "__main__":
    main()

# EOF
