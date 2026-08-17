# Cree una clase LinkedList con los métodos:
# insert_front(data): Inserta al inicio
# insert_back(data): Inserta al final
# delete(data): Elimina el primer nodo con el valor dado
# print_all(): Imprime todos los valores


class Node:#creacion de la clase nodo junto con su constructor
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node

    def __init__(self):
        self.head = None


    def insert_front(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            next_node = self.head
            self.head = node
            node.next = next_node


    def insert_back(self, data):
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
                else:
                    previous_node.next = next_node


    def print_all(self):
        my_string = ""
        current_node = self.head
        while(current_node is not None):
            if current_node.next is None:
                my_string += str(current_node.data)
            else:
                my_string += str(current_node.data) + " -> "
            current_node=current_node.next
        print(my_string)


ll = LinkedList()


ll.insert_front(10)
ll.insert_back(30)
ll.insert_back(50)
ll.insert_front(20)

ll.delete(30)  
# ll.delete(99) 

ll.print_all()


