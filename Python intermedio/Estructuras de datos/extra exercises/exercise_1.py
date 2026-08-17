# Cree una estructura que represente una cola básica (Queue) con objetos enlazados
# Restricción:
# no usar list, dict, tuple, collections
# Métodos requeridos:
# enqueue(data): agrega un nodo al final
# dequeue(): elimina y retorna el nodo del inicio
# print_all(): imprime todos los elementos de la cola en orden


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList():

    def __init__(self):
        self.head = None


class Queue(LinkedList):

    def enqueue(self, data):
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
        

    def dequeue(self):
        if self.head is None:
            raise Exception("Nothing to dequeue, the queue is empty!")
        else:
            current_head = self.head
            self.head = self.head.next
            return current_head.data        

    def print_all(self):
        my_string = ""
        current_node = self.head
        while(current_node is not None):
            if current_node.next is None:
                my_string += current_node.data
            else:
                my_string += current_node.data + " -> "
            current_node=current_node.next
        print(my_string)


queue = Queue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print(queue.dequeue())

print("***********")
queue.print_all()
