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

    def insert_in_order(self, data):
        node = self.head
        if not self.head:
            self.head = LinkedListNode(data)
        elif self.head.data >= data:
            self.head = LinkedListNode(data)
            self.head.next_node = node
        else:
            while node.next_node:
                if node.next_node.data >= data:
                    temp = node.next_node
                    new_node = LinkedListNode(data)
                    node.next_node = new_node
                    new_node.next_node = temp
                    return
                node = node.next_node
            node.next_node = LinkedListNode(data)



def run_tests():
    ll = SinglyLinkedList()
    vals = [1,5,3,2,4,5]

    ll.insert_in_order(1)
    print(ll)
    assert ll.__repr__() == '1'

    ll.insert_in_order(3)
    print(ll)
    assert ll.__repr__() == '1 => 3'

    ll.insert_in_order(4)
    print(ll)
    assert ll.__repr__() == '1 => 3 => 4'

    ll.insert_in_order(2)
    print(ll)
    assert ll.__repr__() == '1 => 2 => 3 => 4'

    ll.insert_in_order(0)
    print(ll)
    assert ll.__repr__() == '0 => 1 => 2 => 3 => 4'

    from random import randint

    for num in [randint(0,100) for num in range(100)]:
        ll.insert_in_order(num)

    head = ll.head
    print(ll)
    while head.next_node:
        assert head.next_node.data >= head.data
        head = head.next_node