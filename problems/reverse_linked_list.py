from ds.py.linked_list import LinkedList
from random import randint

def reverse_linked_list(l):
    current = l.head
    previous = None
    while current:
        next_node = current.next_node
        current.next_node = previous
        previous = current
        current = next_node
    l.head = previous

if __name__ == '__main__':
    l = LinkedList()
    [l.insert(randint(0, 10)) for _ in range(10)]
    print(l)
    reverse_linked_list(l)
    print(l)
