class Queue:
  def __init__(self, head_value = None, max_length = 100):
    self.head =  Node(head_value) if head_value is not None else None
    self.tail = None
    self.length = 0 if not self.head else 1
    self.max_length = max_length

  def enqueue(self, value):
    node = Node(value)
    if self.length == self.max_length:
      raise Exception(f"Enqueue not possible, Queue at capacity, max length: {self.max_length}")
    if self.head:
      node.next_node = self.head
      self.tail = node
      self.length += 1
      return node
    self.head = node
    self.length += 1
    return node

  def peek(self):
    if self.is_empty():
      raise Exception("Queue is empty")
    return self.head.value

  def dequeue(self):
    if self.is_empty():
      raise Exception("Dequeue Not Possible, queue is empty")
    if self.length == 1:
      head = self.head
      self.head = None
      self.length -= 1
      return head.value
    node = self.tail
    while True:
      if node.next_node == self.head:
        previous_head = self.head
        node.next_node == None
        self.head = node
        self.length -= 1
        return previous_head.value
      node = node.next_node

  def is_empty(self):
    return True if self.length == 0 else False

class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None