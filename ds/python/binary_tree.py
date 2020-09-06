from random import random
import math

class Tree:
  def __init__(self, root = None):
    self.root = root

  def insert(self, data):
    if self.root:
      return self.root.insert(self.root, data)
    else:
      self.root = Node(data)
      return True
    return False

  def search(self, value):
    if self.root:
      return self.root.search(self.root, value)
    return None

  def traverse(self):
    if self.root:
      return self.root.traverse_in_order(self.root)
    return None

  def delete(self, value):
    node = self.search(value)
    
    if node:
      node.delete()

  def traverse_iterativeley(self, node):
    # print(node.value)
    while node.left:
      node = node.left
      # print(node.value)
      if node.left == None:
        print(node.value)
        node.parent.left = None
        node = node.parent
        print(node.value)
        node = node.right
        break


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
      node.traverse_in_order(node.left)
    node.perform_operation()
    if node.right:
      node.traverse_in_order(node.right)

  def traverse_pre_order(self, node):
    if node == None:
      return
    node.perform_operation()
    if node.left:
      node.traverse_pre_order(node.left)
    if node.right:
      node.traverse_pre_order(node.right)

  def traverse_post_order(self, node):
    if node == None:
      return
    if node.left:
      node.traverse_post_order(node.left)
    if node.right:
      node.traverse_post_order(node.right)
    node.perform_operation()

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
      return node.insert(node.left, value)
    if node.value < value:
      if node.right == None:
        node.right = Node(value, node)
        return node.right
      return node.insert(node.right, value)
    if node.value == value:
      print(f"Node Value and Value to be inserted are equal Value! Skipping. Value: {node.value}")

  def delete(self):
    if self.is_leaf():
      if self.is_left_child_of_parent():
        self.parent.left = None
      self.parent.right = None
      return self

    if self.has_one_child():
      if self.is_left_child_of_parent():
        if self.has_only_left_child():
          self.parent.left = self.left
          self.left.parent = self.parent
          return self
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
