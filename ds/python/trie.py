import re

class Trie:
  def __init__(self):
    self.root = Node("Root")

  def insert_word(self, word):
    letters_array = [char for char in word]
    self.insert_recursively(self.root, letters_array)

  def insert_recursively(self, node, word):
    if node.value == False:
      return
    current_char = False if word == [] else word[0]
    current_node = Node(current_char)
    if current_char in node.children:
      return self.insert_recursively(node.children[current_char], word[1:])
    else:
      node.children[current_char] = current_node
      return self.insert_recursively(node.children[current_char], word[1:])
  
  def search(self, word):
    letters_array = [char for char in word]
    node = self.root
    for letter in letters_array:
      if letter in node.children:
        node = node.children[letter]
      else:
        return False
    return word if False in node.children else False

  def insert(self, word):
    letters_array = [char for char in word]
    node = self.root
    for letter in letters_array:
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
    trie = Trie()
    trie.insert(word)
    prefix_array = [char for char in prefix]
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

sentence = "Regular expressions can also be used to remove any non alphanumeric characters. re.sub(regex, string_to_replace_with, original_string) will substitute all non alphanumeric characters with empty string. For example"
sentence.isalnum()
print(sentence)
t = Trie()

t.insert("an")
t.insert("abc")
t.insert("abacus")
t.insert("aboration")
t.insert("abracadabra")
t.insert("absolutely")


print(t.contains("ab")) # should this be true??
print(t.search("ab"))
print(t.is_prefix("hello", "hel"))