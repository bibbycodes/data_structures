class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None
    
    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self, head = None, values = None):
        self.head = head
        self.tail = head
        self.values = values
        if self.values:
            self.insert_values()

    def insert(self, data):
        if not self.head:
            self.head = self.tail = LinkedListNode(data)
        else:
            self.tail.next_node = self.tail = LinkedListNode(data)
                    
    def insert_values(self):
        for value in self.values:
            self.insert(value)

    def insert_values_in_order(self, values):
        for value in values:
            self.insert_in_order(value)

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next_node
        else:
            node = self.head
            previous = None
            while node.data != data:
                previous = node
                node = node.next_node
            previous.next_node = node.next_node

    def search(self, data):
        node = self.head
        while node.next_node:
            if node.data == data:
                return node
            node = node.next_node
        raise Exception("Data not found")

    def __repr__(self):
        if self.head:
            node = self.head
            node_string = str(node.data)
            while node.next_node:
                node_string = node_string + f" => {node.next_node.data}"
                node = node.next_node
            return node_string
        return "None"

ll = SinglyLinkedList()
values = [3,2,4,5]
ll.insert_values_in_order(values)
print(ll)