from random import random
import math

class Tree:
  def __init__(self, root = None):
    self.root = root

  def insert(self, data):
    if self.root:
      return self.root.insert(self.root, data) # Improve this line
    else:
      self.root = Node(data)
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

  def traverse_in_order(self, node):
    if node == None:
      return
    if node.left:
      self.traverse_in_order(node.left)
    node.perform_operation()
    if node.right:
      self.traverse_in_order(node.right)

  def search(self, node, value):
    if node == None:
      return
    if node.value == value:
      return node
    if node.value < value:
      return self.search(node.right, value)
    if node.value > value:
      return self.search(node.left, value)

  def insert(self, node, value):
    if node == None:
      node = Node(value)
      return node
    if node.value > value:
      if node.left == None:
        node.left = Node(value, node)
        return node.left
      else:
        return node.insert(node.left, value)
    if node.value < value:
      if node.right == None:
        node.right = Node(value, node)
        return node.right
      else:
        return node.insert(node.right, value)
    if node.value == value:
      print(f"Node Value and Value to be inserted are equal Value! Skipping. Value: {node.value}")

  def delete(self):
    if self.is_leaf():
      if self.is_left_child_of_parent():
        self.parent.left = None
      else:
        self.parent.right = None

    if self.has_one_child():
      if self.is_left_child_of_parent():
        if self.has_only_left_child() is True:
          self.parent.left = self.left
          self.left.parent = self.parent
          return self
        elif self.has_only_left_child() is False:
          self.parent.left = self.right
          self.right.parent = self.parent
          return self

      else:
        if self.has_only_left_child() is True:
          self.parent.right = self.left
          self.left.parent = self.parent
          return self
        self.right.parent = self.parent
        return self

    if self.has_two_children():
      left_most_node = self.get_leftmost_node_of_right_sub_tree(self.right)
      left_most_node.parent = self.parent
      left_most_node.left = self.left
      self.left.parent = left_most_node
      return self


  def is_leaf(self):
    if not self.left and not self.right:
      return True
    return False

  def is_left_child_of_parent(self):
    if self.parent.left.value == self.value:
      return True
    if self.parent.right.value == self.value:
      return False

  def has_one_child(self):
    if self.left and not self.right:
      return True
    if self.right and not self.left:
      return True
    return False

  def has_only_left_child(self):
    if self.left and not self.right:
      return True
    if self.right and not self.left:
      return False

  def has_two_children(self):
    if self.left and self.right:
      return True
    return False

  def get_parent(self, node):
    return self.parent

  def get_leftmost_node_of_right_sub_tree(self, right_node):
    if right_node.left == None:
      return right_node
    return self.get_leftmost_node_of(node.left)

  def perform_operation(self):
    print(self.value)
    return self.value

tree = Tree()
tree.insert(4)
tree.insert(2)
tree.insert(6)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(7)
tree.insert(9)
tree.insert(8)
deleted_node = tree.delete(6)
tree.search(6)
node = tree.search(5)
node = tree.search(9)

print("node.value", node.value) 
print("node.parent.value", node.parent.value,)
print("node.left.value", node.left.value,)
print("node.left.value", node.left.value,)
print("node.parent.right.value", node.parent.right.value,)
print("node.parent.left.value", node.parent.left.value)

# node = tree.search(8)
# print(node.get_leftmost_node_of(node).value)


# tree.insert(10)
# tree.search(8)
# tree.delete(8)
# tree.search(8)
# tree.insert(6)
# tree.insert(10)
# tree.search(3)
# tree.insert(3)

# tree.search(6)
# tree.delete(8)
# for i in range(1000):
#   value = math.floor(random() * 1000)
#   tree.insert(value)

# tree.traverse()
# print(tree.root.value)
