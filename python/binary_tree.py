from random import random
import math

class Tree:
  def __init__(self, root = None):
    self.root = root

  def insert(self, data):
    if self.root:
      print(f"Root exists. Value: {self.root.value}")
      return self.root.insert(self.root, data) # Improve this line
    else:
      self.root = Node(data)
      print(f"Created tree root with value {self.root.value}")
      return True
    return False

  def search(self, value):
    if self.root:
      return self.root.search(self.root, value)
    else:
      return None

  def traverse(self):
    if self.root:
      return self.root.traverse_in_order(self.root)
    else:
      return None

  def delete(self, value):
    node = self.search(value)
    if node:
      print(node)
      node.delete()

class Node:
  def __init__(self, value, parent=None):
    self.left = None
    self.right = None
    self.value = value
    self.parent = parent

  def delete(self):
    print(self)

  def is_leaf(self):
    if not self.left and not self.right:
      return True
    return False

  def has_one_child(self):
    if self.left and not self.right:
      return True
    if self.right and not self.left:
      return True
    return False

  def has_two_children(self):
    if self.left and self.right:
      return True
    return False

  def get_parent(self, node):
    return self.parent

  def traverse_in_order(self, node):
    if node == None:
      print("Node == None, Returning")
      return
    if node.left:
      print("Visiting left node")
      self.traverse_in_order(node.left)
    print("Performing Operation, visiting node")
    node.perform_operation()
    if node.right:
      print("Visiting right node")
      self.traverse_in_order(node.right)
    print("Reached Leaf Node")

  def search(self, node, value):
    if node == None:
      print("Value does not exist in tree")
      return
    if node.value == value:
      print(f"Found {value} at {node} with parent value {node.parent.value if node.parent != None else None}")
      return node
    if node.value < value:
      print(f"Current node value {node.value} < Value to be searched: {value}, Searching Right")
      return self.search(node.right, value)
    if node.value > value:
      print(f"Current node value {node.value} > Value to be searched: {value}, Searching Left")
      return self.search(node.left, value)

  def insert(self, node, value):
    print(f"Starting insert recursion with value: {value} through node with value: {node.value}")
    if node == None:
      print("Node is None")
      node = Node(value)
      return
    if node.value > value:
      print(f"Current node Value: {node.value} > Value to be inserted: {value}")
      if node.left == None:
        print(f"Creating new node with value: {value} to the left of node with Value: {node.value}")
        node.left = Node(value, node)
        return
      else:
        print(f"Recursing through function. Going left. Value to be inserted: {value}")
        node.insert(node.left, value)
    if node.value < value:
      print(f"Current node Value {node.value} < Value to be inserted: {value}")
      if node.right == None:
        print(f"Creating new node with value: {value} to the left of node with Value: {node.value}")
        node.right = Node(value, node)
        return
      else:
        print(f"recursing insert {value} right")
        node.insert(node.right, value)
    if node.value == value:
      print(f"Node Value and Value to be inserted are equal Value! Skipping. Value: {node.value}")
    print("Reached end of recursion")

  def perform_operation(self):
    print(self.value)
    return self.value

tree = Tree()
tree.insert(3)
tree.insert(8)
tree.insert(2)
tree.insert(6)
tree.insert(10)
tree.search(3)
# tree.insert(3)

# tree.search(6)
# tree.delete(8)
# for i in range(1000):
#   value = math.floor(random() * 1000)
#   tree.insert(value)

# tree.traverse()
# print(tree.root.value)
