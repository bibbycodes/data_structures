# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        stack = deque()
        stack.appendright(root)
        while node.left or node.right:
            if node.left:
                node = node.left
            else:
                node = node.right
            stack.appendright(node)
            self.slot_in_before_parent()

    
    def find_right_most_from_left(self, node):
        if not node.left:
            return node
        node = node.left
        while node.right:
            node = node.right
        return node

    def slot_in_before_parent(self, parent, node):
        temp_right = parent.right
        temp_left = parent.left
        node.left = parent.left
        node.right = parent
        return node