from random import random
import math
class Tree:
  def __init__(self, root = None):
    self.root = root

  def insert(self, data):
    if self.root:
      # print(f"root exists, value {self.root.value}")
      # print(f"node value {node.value}, root value {self.root.value}")
      return self.root.insert(self.root, data)
    else:
      self.root = Node(data)
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
      print("returning")
      return
    if node.left:
      print("going left")
      self.traverse_in_order(node.left)
    print("Performing Operation")
    node.perform_operation()
    if node.right:
      print("going right")
      self.traverse_in_order(node.right)
    print("Reached end")

  # def visit(self, node):
  #   if self.left != None:
  #     return self.visit(self.left)
  #   elif self.right != None:
  #     return self.visit(self.right)
  #   else:
  #     self.perform_operation(operation)

  def insert(self, node, value):
    print(f"begin insert {value} through {node.value}")
    if node == None:
      print("node is None")
      node = Node(value)
      return
    if node.value > value:
      print(f"Current node Value {node.value} > Value {value}")
      if node.left == None:
        print(f"creating node of value {value} left")
        node.left = Node(value)
        return
      else:
        print(f"recursing insert {value} left")
        node.insert(node.left, value)
    if node.value < value:
      print(f"Current node Value {node.value} < Value {value}")
      if node.right == None:
        print(f"creating node of value {value} right")
        node.right = Node(value)
        return
      else:
        print(f"recursing insert {value} right")
        node.insert(node.right, value)
    if node.value == value:
      print("Equal Value! Skipping")
    print("Reached end of function")
      
  def perform_operation(self):
    print(self.value)
    return self.value

tree = Tree()
for i in range(100):
  value = math.floor(random() * 100)
  tree.insert(value)

tree.traverse()
# print(tree.root.value)
