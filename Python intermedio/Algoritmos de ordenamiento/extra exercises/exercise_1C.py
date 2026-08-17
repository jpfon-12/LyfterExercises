# Implemente un bubble_sort que funcione para los ejercicios de estructura de datos:

# Cree una estructura de objetos que asemeje un Binary Tree.
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    data: str
    right: "Node"
    left: "Node"

    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left


class BinaryTree:
    root: Node

    def __init__(self, root):
        self.root = root


    def print_tree(self, node):
        if node is None: 
            return
        else:
            print(node.data)
        self.print_tree(node.right)
        self.print_tree(node.left)


    def make_one_pass(self, node, previous_node):
        if node is None:
            return previous_node

        #compare the previous node with the current node and swap the values using a temporary variable
        if previous_node is not None: 
            if previous_node.data > node.data:
                temp_value = previous_node.data
                previous_node.data = node.data
                node.data = temp_value

                self.has_made_changes = True #a change happened in this pass.

        #the current node becomes the "previous node" for the rest
        previous_node = node

        #continue the traversal, carrying the updated previous_node.
        previous_node = self.make_one_pass(node.right, previous_node)
        previous_node = self.make_one_pass(node.left, previous_node)

        return previous_node

    def bubble_sort(self):
        # keep making full passes until a pass makes no changes.
        while True:
            self.has_made_changes = False
            self.make_one_pass(self.root, None)

            if self.has_made_changes is False:
                break


fifth_node = Node(5)
fourth_node = Node(4)
third_node = Node(3)
second_node = Node(2, fourth_node, fifth_node)
first_node = Node(1, second_node, third_node)

bt = BinaryTree(first_node)
bt.print_tree(bt.root)

bt.bubble_sort()

print("---")
bt.print_tree(bt.root)
