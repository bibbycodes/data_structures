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
    return word

class Node:
  def __init__(self, value):
    self.value = value
    self.children = {}


t = Trie()
t.insert_word("an")
t.insert_word("abc")
t.insert_word("abacus")
t.insert_word("aboration")
t.insert_word("abracadabra")
t.insert_word("absolutely")
print(t.root)
print(t.root.children)
print(t.root.children['a'].children)
print(t.root.children['a'].children['b'].children)
print(t.root.children['a'].children['b'].children['a'].children)
print(t.root.children['a'].children['b'].children['a'].children['c'].children)
print(t.root.children['a'].children['b'].children['a'].children['c'].children['u'].children)
print(t.root.children['a'].children['b'].children['a'].children['c'].children['u'].children['s'].children)
print(t.search("abacus"))