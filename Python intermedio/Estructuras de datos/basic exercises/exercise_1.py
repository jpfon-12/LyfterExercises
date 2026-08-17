# Cree una estructura de objetos que asemeje un Stack.
# Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.


class Node:#creacion de la clase nodo junto con su constructor
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


first_node = Node("Dirty dish 1" )
second_node = Node("Dirty dish 2", first_node)
third_node = Node("Dirty dish 3", second_node)
forth_node = Node("Dirty dish 4", third_node)



stack = Stack(forth_node)
stack.print_structure()
stack.push(Node("New dirty dish"))
print('--------------')
stack.print_structure()
print('calling pop()------')
print(f"Item deleted: {stack.pop()}")
print('****')
stack.print_structure()

