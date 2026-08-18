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

def print_inorder(tree):
    if tree is not None:
        print_inorder(tree.left_child)
        print(tree.value, end=" ")
        print_inorder(tree.right_child)

def print_preorder(tree):
    if tree is not None:
        print(tree.value, end=" ")
        print_preorder(tree.left_child)
        print_preorder(tree.right_child)

def print_postorder(tree):
    if tree is not None:
        print_postorder(tree.left_child)
        print_postorder(tree.right_child)
        print(tree.value, end=" ")

def find_node(tree, value):
    if tree is None:
        return False

    if tree.value == value:
        return True

    if value < tree.value:
        return find_node(tree.left_child, value)
    else:
        return find_node(tree.right_child, value)


numbers = [50, 30, 70, 20, 40, 60, 80, 10]

binary_tree = None

for number in numbers:
    binary_tree = add_node(binary_tree, number)


print("Inorder traversal:")
print_inorder(binary_tree)

print("\nPreorder traversal:")
print_preorder(binary_tree)

print("\nPostorder traversal:")
print_postorder(binary_tree)


sorted_values = []

def save_inorder(tree):
    if tree is not None:
        save_inorder(tree.left_child)
        sorted_values.append(tree.value)
        save_inorder(tree.right_child)

save_inorder(binary_tree)


if sorted_values == sorted(sorted_values):
    print("\n\nInorder traversal is in sorted order.")
else:
    print("\n\nInorder traversal is not in sorted order.")


search_value1 = 60

if find_node(binary_tree, search_value1):
    print(search_value1, "found in the BST.")
else:
    print(search_value1, "not found in the BST.")


search_value2 = 100

if find_node(binary_tree, search_value2):
    print(search_value2, "found in the BST.")
else:
    print(search_value2, "not found in the BST.")
