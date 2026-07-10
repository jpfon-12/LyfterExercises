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


fifth_node = Node("Fifth node")
fourth_node = Node("Fourth node")
third_node = Node("Third node")
second_node = Node("Second node", fourth_node, fifth_node)
first_node = Node("First node", second_node, third_node)

bt = BinaryTree(first_node)
bt.print_tree(bt.root)




