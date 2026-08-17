# Implemente un bubble_sort que funcione para los ejercicios de estructura de datos:

# Cree una estructura de objetos que asemeje un Double Ended Queue.
# Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de 


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


deq = DoubleEndedQueue(node_f)

print("Queue original")
deq.print_structure()



print("---adding at the end of the q---")
deq.push_right(Node(100))
deq.print_structure()

print("---adding at the beginning of the q------")
deq.push_left(Node(500))
deq.print_structure()


print("---------")
print("Queue after sorting")
deq.bubble_sort()
deq.print_structure()

