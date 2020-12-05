from collections import deque

class Solution:
    def __init__(self):
        self.levels = {}
        self.result = []

    def zigzag(self, root):
        res = []
        queue = deque()
        queue.append(root)
        h = 0

        while queue:
            arr = []
            for item in queue:
                arr.append(item)
            for _ in arr:
                item = queue.popleft
                queue.append(item.left)
                queue.append(item.right)
            
            if h % 2 == 0:
                res.append(arr)
            else:
                res.append(reversed(arr))
            h += 1
        
        return res