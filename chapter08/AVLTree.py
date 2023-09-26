class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.bf = 0

    def __repr__(self):
        return f"{self.val}"

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __le__(self, other):
        return self.val <= other.val

    def __eq__(self, other):
        return self.val == other.val

    def is_leaf(self):
        return not (self.left or self.right)


class AVLTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def get_height(root):
        return root.height if root else 0

    @staticmethod
    def update_height(root):
        root.height = 1 + max(
            AVLTree.get_height(root.left),
            AVLTree.get_height(root.right)
        )

    @staticmethod
    def right_rotation(root: Node):
        final_root = root.left
        left_right_node = root.left.right
        final_root.right = root
        root.left = left_right_node

        AVLTree.update_height(root)
        AVLTree.update_height(final_root)

        return final_root

    @staticmethod
    def left_rotation(root: Node):
        final_root = root.right
        right_left_node = root.right.left
        final_root.left = root
        root.right = right_left_node

        AVLTree.update_height(root)
        AVLTree.update_height(final_root)

        return final_root

    def insert(self, val):
        def recursive_insert(root, node):
            # bst insert
            if not self.root:
                self.root = node
                return node
            if not root:
                return node
            if root:
                if node < root:
                    root.left = recursive_insert(root.left, node)
                else:
                    root.right = recursive_insert(root.right, node)

            AVLTree.update_height(root)
            root = AVLTree.re_balance(root)

            return root

        new_node = Node(val)
        self.root = recursive_insert(self.root, new_node)

    @staticmethod
    def re_balance(local_root):
        if not local_root:
            return None
        left_child_height = AVLTree.get_height(local_root.left if local_root else None)
        right_child_height = AVLTree.get_height(local_root.right if local_root else None)
        local_root.bf = left_child_height - right_child_height

        if local_root.bf > 1:  # heavy left
            if (local_root.left.bf if local_root.left else 0) < 0:
                local_root.left = AVLTree.left_rotation(local_root.left)
            local_root = AVLTree.right_rotation(local_root)
        elif local_root.bf < -1:  # heavy right
            if (local_root.right.bf if local_root.right else 0) > 0:
                local_root.right = AVLTree.right_rotation(local_root.right)
            local_root = AVLTree.left_rotation(local_root)
        AVLTree.update_height(local_root)
        return local_root

    def traverse(self):
        def in_order(node, level=0):
            if node:
                in_order(node.right, level + 1)
                print('     ' * level, node)
                in_order(node.left, level + 1)

        in_order(self.root)

    def delete(self, data):
        def _delete(root: Node, key):
            if root is None:
                return root
            if int(key) < int(root.val):
                root.left = _delete(root.left, key)
            elif int(key) > int(root.val):
                root.right = _delete(root.right, key)
            else:
                if root.left is None or root.right is None:
                    root = root.left if root.right is None else root.right
                else:
                    temp = root.left
                    while temp.right is not None:
                        temp = temp.right
                    root.val = temp.val
                    root.left = _delete(root.left, temp.val)
            root = self.re_balance(root)
            return root

        self.root = _delete(self.root, data)
