class Queue:
  def __init__(self, head_value = None, max_length = 100):
    self.head =  Node(head_value) if head_value is not None else None
    self.tail = None
    self.length = 0 if self.head == None else 1
    self.max_length = max_length

  def enqueue(self, value):
    if self.head:
      if self.length == self.max_length:
        print(f"Enqueue not possible, Queue at capacit: {self.max_length}")
      node = Node(value)
      node.next_node = self.head
      self.head = node
      self.length += 1
      return self.head
    self.head = Node(value)
    self.length += 1
    return self.head

  def dequeue(self):
    if self.head.next_node == None:
      self.head = None
      return self.head
    return self.head.dequeue(self.head)

class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None

  def dequeue(self, node, previous_node = None):
    if node.next_node == None:
      previous_node.next_node = None
      return node
    return node.dequeue(node.next_node, node)


q = Queue()
q.enqueue(10)
q.enqueue(34)
q.enqueue(32)
q.enqueue(37)
q.enqueue(111)
print(q.dequeue().value)
# print(q.head.next_node.value)
print(q.head.value)