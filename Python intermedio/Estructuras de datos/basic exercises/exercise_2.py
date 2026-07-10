# Cree una estructura de objetos que asemeje un Double Ended Queue.
# Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.


class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList():
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next


class DoubleEndedQueue(LinkedList):

    def push_right(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            next_node = current_node.next
            while(next_node is not None):
                current_node = next_node
                next_node = current_node.next 
            current_node.next = new_node


    def push_left(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    def pop_right(self):
        if self.head is None:
            raise Exception("Cannot pop from an empty queue")
        else:
            if self.head.next is None:
                self.head = None
            else:
                current_node = self.head
                next_node = current_node.next
                while(next_node.next is not None):
                    current_node = next_node
                    next_node = current_node.next
                    #print(f"current: {current_node.data}, next: {next_node.data}")
                current_node.next = None
            
            

    def pop_left(self):
        if self.head is None:
            raise Exception("Cannot pop from an empty queue")
        else:
            self.head = self.head.next


second_node = Node("I'm second node")
first_node = Node("I'm the first node", second_node)


deq = DoubleEndedQueue(first_node)

deq.print_structure()

print("-----------------------")
deq.push_right(Node("I will put myself at the end"))
deq.print_structure()

print("------------------")
deq.push_left(Node("I'll put myself in first position"))
deq.print_structure()
print("------------------")

deq.pop_left()
deq.print_structure()

print("--------------")
deq.pop_right()
deq.print_structure()