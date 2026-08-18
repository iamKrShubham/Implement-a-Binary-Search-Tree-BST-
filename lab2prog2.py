class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def add_node(tree, value):
    if tree is None:
        return TreeNode(value)

    if value < tree.value:
        tree.left_child = add_node(tree.left_child, value)
    elif value > tree.value:
        tree.right_child = add_node(tree.right_child, value)

    return tree


def display_inorder(tree):
    if tree is not None:
        display_inorder(tree.left_child)
        print(tree.value, end=" ")
        display_inorder(tree.right_child)


def get_minimum(tree):
    current_node = tree

    while current_node.left_child is not None:
        current_node = current_node.left_child

    return current_node


def remove_node(tree, value):

    if tree is None:
        return None

    if value < tree.value:
        tree.left_child = remove_node(tree.left_child, value)

    elif value > tree.value:
        tree.right_child = remove_node(tree.right_child, value)

    else:

        # Case 1: Node is a leaf
        if tree.left_child is None and tree.right_child is None:
            return None

        # Case 2: Node has only a right child
        elif tree.left_child is None:
            return tree.right_child

        # Case 3: Node has only a left child
        elif tree.right_child is None:
            return tree.left_child

        # Case 4: Node has two children
        else:
            successor_node = get_minimum(tree.right_child)
            tree.value = successor_node.value

            tree.right_child = remove_node(
                tree.right_child, successor_node.value
            )

    return tree


values = [50, 30, 70, 20, 40, 60, 80, 10]

binary_tree = None

for number in values:
    binary_tree = add_node(binary_tree, number)


print("Original BST:")
display_inorder(binary_tree)
print()


print("\nAfter deleting leaf node 40:")
binary_tree = remove_node(binary_tree, 40)
display_inorder(binary_tree)
print()


print("\nAfter deleting node 20 (one child):")
binary_tree = remove_node(binary_tree, 20)
display_inorder(binary_tree)
print()


print("\nAfter deleting node 50 (two children):")
binary_tree = remove_node(binary_tree, 50)
display_inorder(binary_tree)
print()
