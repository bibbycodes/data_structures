# Write Code to remove duplicates from an unsorted linked list
# How would you solve this problem without using a temporary buffer?

from ds.py.linked_list import LinkedList, Node

def remove_dups(linked_list):
    buffer = {}
    node = linked_list.head
    previous = Node(None)
    while node:
        if node.value in buffer:
            previous.next_node = node.next_node
        else:
            buffer[node.value] = True
            previous = node
        node = node.next_node
    return linked_list

# To do this without a temporary buffer, 
# we could use two[i,j] pointers to traverse the list in 0(n2) time

def remove_dups_without_buffer(linked_list):
    ith_node = linked_list.head
    while ith_node.next_node:
        jth_node = ith_node
        while jth_node.next_node:
            if ith_node.value == jth_node.next_node.value:
                jth_node.next_node = jth_node.next_node.next_node
            else:
                jth_node = jth_node.next_node
        ith_node = ith_node.next_node

ll_1 = LinkedList()
ll_2 = LinkedList()
values = [1,2,3,4,1,4,5]

for num in values:
    ll_1.insert(num)
    ll_2.insert(num)

remove_dups(ll_1)
remove_dups(ll_2)

assert ll_1.__repr__() == "1 => 2 => 3 => 4 => 5"
assert ll_2.__repr__() == "1 => 2 => 3 => 4 => 5"

            
