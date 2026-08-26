# Implemente un bubble_sort que funcione para los ejercicios de estructura de datos:

# Cree una estructura de objetos que asemeje un Stack.
# Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structure(self):
        current_node = self.head
        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next


class Stack(LinkedList):

    def push(self, new_node):
        next_node = self.head
        self.head = new_node
        new_node.next = next_node

    def pop(self):
        current_node = self.head.next    
        deleted_item = self.head    
        self.head = current_node
        return deleted_item.data


    def bubble_sort(self):
            while True:
                has_made_changes = False
                current_node = self.head
                while current_node.next is not None:
                    current_element = current_node.data
                    next_element = current_node.next.data
                    if current_element > next_element:
                        current_node.data = next_element
                        current_node.next.data = current_element
                        has_made_changes = True
                    current_node = current_node.next
                if has_made_changes is False:
                    break



node_a = Node(5)
node_b = Node(2, node_a)
node_c = Node(8, node_b)
node_d = Node(1, node_c)
node_e = Node(9, node_d)
node_f = Node(3, node_e)



stack = Stack(node_f)

print("Stack original:")
stack.print_structure()


print("\nStack sorted:")
stack.bubble_sort()
stack.print_structure()
