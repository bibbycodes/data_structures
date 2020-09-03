class Trie:
  def __init__(self):
    self.root = Node("Root")

  def insert_word(self, word):
    letters_array = [char for char in word]
    self.insert_recursively(self.root, letters_array)

  def insert_recursively(self, node, word):
    if node.value == False:
      return
    current_char = word[0] if word != [] else False
    current_node = Node(current_char)
    if current_char in node.children:
      return self.insert_recursively(node.children[current_char], word[1:])
    else:
      node.children[current_char] = current_node
      return self.insert_recursively(node.children[current_char], word[1:])



class Node:
  def __init__(self, value):
    self.value = value
    self.children = {}

  # def insert(self, letter, letters_array):
  #   if letter is None:
  #     return
  #   if letter not in self.children:
  #     letter_node = Node(letter)
  #     self.children[letter] = letter_node
  #     if len(letters_array) > 0:
  #       return letter_node.insert(letters_array[0], letters_array[1:])
  #   else:
  #     letters_array = letters_array[1:]
  #     return self.children[letter].insert(letters_array[0], letters_array[:1])

  # def insert(self, node, word_array):
  #   if node.value == None or word_array == []:
  #     node.word_end = True
  #     return
  #   if node.value not in node.children:
  #     new_node = Node(word_array[0])
  #     node.children[word_array[0]] = new_node
  #     if len(word_array) > 0:
  #       return node.insert(new_node, word_array[1:])
  #   else:
  #     node = Node(node.children[node.value])
  #     new_node = Node(word_array[0])
  #     return node.insert(new_node, word_array[1:])


t = Trie()
t.insert_word("an")
t.insert_word("abc")
t.insert_word("abacus")
t.insert_word("absolutely")
print(t.root)
print(t.root.children)
print(t.root.children['a'].children)
print(t.root.children['a'].children['b'].children)
print(t.root.children['a'].children['b'].children['a'].children)
print(t.root.children['a'].children['b'].children['a'].children['c'].children)
print(t.root.children['a'].children['b'].children['a'].children['c'].children['u'].children)
print(t.root.children['a'].children['b'].children['a'].children['c'].children['u'].children['s'].children)