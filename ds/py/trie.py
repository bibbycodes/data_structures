import re

class Trie:
  def __init__(self):
    self.root = Node("Root")

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

  def is_substring(self, s1, s2):
    s1, s2 = s1.lower(), s2.lower()
    trie = Trie()
    trie.insert(s1)
    node = trie.root
    j = 0

    for letter in s1:
      if j == len(s2):
        return True
      if s2[j] in node.children:
        j += 1
      node = node.children[letter]
    return False

class Node:
  def __init__(self, value):
    self.value = value
    self.children = {}

t = Trie()

print(t.is_substring("hello", "hell"))