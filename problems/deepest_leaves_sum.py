# Given a binary tree, return the sum of values of its deepest leaves.
# input: root = [1,2,3,4,5,None,6,7,None,None,None,None,8]
# Output 15

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  # def deepestLeavesSum(self, root: TreeNode) -> int:

  def get_left_child_index(self, index):
    return (index * 2) + 1

  def get_right_child_index(self, index):
    return (index * 2) + 2

  def traverse(self, ArrayRepr, index = 0, counter = 0):
    if ArrayRepr[index] == None:
      return
    
    left_index = self.get_left_child_index(index)
    right_index = self.get_right_child_index(index)
    
    if left_index < len(ArrayRepr):
      if ArrayRepr[left_index]:
        print(ArrayRepr[left_index])
        return self.traverse(ArrayRepr, left_index, counter + 1)

    print(ArrayRepr[index])

    if right_index < len(ArrayRepr):
      if ArrayRepr[right_index]:
        print(ArrayRepr[right_index])
        return self.traverse(ArrayRepr, left_index, counter + 1)

root = [1,2,3,4,5,None,6,7,None,None,None,None,8]
s = Solution()
s.traverse(root)
    

