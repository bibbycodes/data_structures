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

  def traverse(self):
    if self.root:
      return self.root.traverse_in_order(self.root)
    else:
      return None

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

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
        node.left = Node(value)
        return
      else:
        print(f"Recursing through function. Going left. Value to be inserted: {value}")
        node.insert(node.left, value)
    if node.value < value:
      print(f"Current node Value {node.value} < Value to be inserted: {value}")
      if node.right == None:
        print(f"Creating new node with value: {value} to the left of node with Value: {node.value}")
        node.right = Node(value)
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
for i in range(1000):
  value = math.floor(random() * 1000)
  tree.insert(value)

tree.traverse()
# print(tree.root.value)
