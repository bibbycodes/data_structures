# Write code to partition a linked list around a value x such that all nodes less than x come 
# before all nodes greater than or equal to x. 
# Important! The partition element x can appear anywhere in the right partition. 
# It does not need to appeear between the left and right partitions. 
# EG input 3 => 5 => 8 => 5 => 10 => 2 => 1 (partition = 5)
# Ou
import sys
import os
sys.path.append(os.path.abspath('../ds/py'))

from ds.linked_list import LinkedList

def partition_linked_list(ll, partition_value):
    node = ll.head
    right_side = None
    previous = None
    while node:
        if node.value >= partition_value:
            deleted_node = remove_node(node, previous, ll)
            if right_side:
                deleted_node.next_node = right_side
            right_side = deleted_node
            node = previous
        previous = node
        node = node.next_node
    previous.next_node = right_side

def remove_node(node, previous, ll):
    if previous:
        previous.next_node = node.next_node
        node.next_node = None
        return node
    else:
        head = ll.head
        ll.head = ll.head.next_node
        previous = ll.head
        return head

ll = LinkedList()
for val in [3,5,8,5,10,2,1]:
    ll.insert(val)

partition_linked_list(ll, 8)

print(ll)