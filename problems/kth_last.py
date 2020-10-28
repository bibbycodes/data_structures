# Implement an algorithm that returns the kth last element of a singly linked list

from ds.py.linked_list import LinkedList

# time O(n), space O(n)
def kth_last(linked_list, k):
    nodes = []
    node = linked_list.head
    while node:
        nodes.append(node)
        node = node.next_node
    node_values = [node.value for node in nodes]
    return nodes[len(nodes)  - k]

# time O(n), space O(1)
def kth_last_two_pointers(linked_list, k):
    p1 = linked_list.head
    p2 = linked_list.head

    for i in range(k):
        p1 = p1.next_node

    while p1:
        p1 = p1.next_node
        p2 = p2.next_node

    return p2

# time O(n), space O(n)
def print_kth_last(head, k):
    if head == None:
        return 0
    index = print_kth_last(head.next_node, k) + 1
    if index == k:
        print(f"{k}'th to last node = {head.value}")
    return index

ll_1 = LinkedList()

values = [1,2,3,4,1,4,5]

for num in values:
	ll_1.insert(num)

head = ll_1.head

print_kth_last(head, 2)
print_kth_last(head, 1)

assert kth_last(ll_1, 2).value == 4
assert kth_last(ll_1, 1).value == 5

assert kth_last_two_pointers(ll_1, 1).value == 5
assert kth_last_two_pointers(ll_1, 2).value == 4