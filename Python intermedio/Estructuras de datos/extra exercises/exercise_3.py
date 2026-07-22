# Lista doblemente enlazada
# Requisitos:
# Cada nodo debe tener referencia al siguiente y al anterior
# Métodos:
# append(data): Agrega al final
# prepend(data): Agrega al inicio
# delete(data): Elimina el primer nodo con ese valor
# print_forward() y print_backward(): Imprime en ambas direcciones

class Node:#creacion de la clase nodo junto con su constructor

    def __init__(self, data, next=None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:

    def __init__(self):
        self.head = None


    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            next_node = current_node.next
            while(next_node is not None):
                current_node = next_node
                next_node = current_node.next
            current_node.next = node
            node.prev = current_node
        
        
    def prepend(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            next_node = self.head
            self.head = node
            node.next = next_node
            next_node.prev = node


    def delete(self, node_to_delete):
        if self.head is None:
            raise Exception("Nothing to delete, the structure is empty!")
        else:
            current_node = self.head 
            next_node = current_node.next
            previous_node = None
            while(current_node is not None and current_node.data != node_to_delete):
                previous_node = current_node
                current_node = next_node
                if current_node is not None:
                    next_node = current_node.next 
            if current_node is None:
                raise Exception("Node not found!")
            else:
                if previous_node is None:
                    self.head = self.head.next
                    if self.head is not None:
                        self.head.prev = None
                else:
                    if next_node is None:
                        previous_node.next = None
                    else:
                        previous_node.next = next_node
                        next_node.prev = previous_node


    def print_forward(self):
        my_string = ""
        current_node = self.head
        while(current_node is not None):
            if current_node.next is None:
                my_string += current_node.data
            else:
                my_string += current_node.data + " -> "
            current_node=current_node.next
        print(my_string)


    def print_backward(self):
        my_string = ""
        current_node = self.head
        while(current_node.next is not None):
            current_node = current_node.next
        while(current_node is not None):
            if current_node.prev is not None:
                my_string += current_node.data + " -> "
            else:
                my_string += current_node.data 
            current_node = current_node.prev
        print(my_string)
        


dll = DoubleLinkedList()

dll.append("A")
dll.append("B")
dll.append("C")
dll.prepend("Z")

dll.delete("Z")

dll.print_forward()
dll.print_backward()