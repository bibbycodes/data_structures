import re

class Trie:
  def __init__(self):
    self.root = Node("Root")

  def insert_word(self, word):
    self.insert_recursively(self.root.value, word)

  def insert_recursively(self, letter, word):
    node = Node(letter)
    if node.value == False: # Boolean Flag for end of word
      return
    current_char = False if word == '' else word[0] # if word is empty (ie we have reached the end of the word) current_char becomes the termination flag
    current_node = Node(current_char)
    if current_char in node.children: # if char in subtree, keep going down subtree and pass down word with first_char popped
      return self.insert_recursively(node.children[current_char].value, word[1:]) 
    else: # else add char into children, pop off first_char and continue down subtree
      node.children[current_char] = current_node # add node into dict
      return self.insert_recursively(node.children[current_char].value, word[1:]) # repeat with word minus first char of word
  
  def search(self, word):
    node = self.root
    for letter in word:
      if letter in node.children:
        node = node.children[letter]
      else:
        return False
    return word if False in node.children else False

  def insert(self, word):
    node = self.root
    for letter in word:
      if letter in node.children:
        node = node.children[letter]
      else:
        new_node = Node(letter)
        node.children[letter] = new_node
        node = new_node
    node.children[False] = Node(False)

  def contains(self, word):
    return True if self.search(word) is not False else False

  def is_prefix(self, word, prefix):
    word, prefix = word.lower(), prefix.lower()
    trie = Trie()
    trie.insert(word)
    node = trie.root
    for letter in prefix:
      if letter not in node.children:
        return False
      else:
        node = node.children[letter]
    return True

class Node:
  def __init__(self, value):
    self.value = value
    self.children = {}
