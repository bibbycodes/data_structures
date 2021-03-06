# Implement an algorithm that deletes a node in the middle (ie any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node

# eg input: node c from a -> b -> c -> d -> e -> f
# Result: nothing is returned but the new linked list looks like a -> b -> d -> e -> f

from ds.py.linked_list import LinkedList


def delete_middle_node(ll, middle_node):
    if middle_node.next_node == None:
        return False
    next_node = middle_node.next_node
    middle_node.value = next_node.value
    middle_node.next_node = next_node.next_node
    return True

ll = LinkedList()
for item in ['a', 'b', 'c', 'd', 'e', 'f']:
    if item == 'b':
        middle_node = ll.insert(item)
    else:
        ll.insert(item)

delete_middle_node(ll, middle_node)
assert ll.__repr__() == "a => c => d => e => f"