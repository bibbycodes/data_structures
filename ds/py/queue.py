class Queue:
  def __init__(self, head_value = None, max_length = 100):
    self.head =  Node(head_value) if head_value is not None else None
    self.tail = None
    self.length = 0 if not self.head else 1
    self.max_length = max_length

  def enqueue(self, value):
    if self.length == self.max_length:
      print(f"Enqueue not possible, Queue at capacity: {self.max_length}")
      return
    if self.head:
      node = Node(value)
      node.next_node = self.head
      self.head = node
      self.length += 1
      return self.head
    self.head = Node(value)
    self.length += 1
    return self.head

  def peek(self):
    if self.length == 1:
      return self.head
    if self.length < 1:
      return None
    return self.head.peek(self.head)

  def dequeue(self):
    if self.is_empty():
      print(f"Dequeue Not Possible, queue is empty")
    if self.head.next_node == None:
      self.head = None
      return self.head
    return self.head.dequeue(self.head)

  def is_empty(self):
    return True if self.length == 0 else False

class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None

  def dequeue(self, node, previous_node = None):
    if node.next_node == None:
      previous_node.next_node = None
      return node
    return node.dequeue(node.next_node, node)

  def peek(self, node):
    if node.next_node == None:
      return node
    return node.peek(node.next_node)