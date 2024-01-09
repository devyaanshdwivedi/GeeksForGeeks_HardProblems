#User function Template for python3
from collections import deque
import sys
sys.setrecursionlimit(50000)
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        queue = deque([root])
        temp = []
        while queue:
            node = queue.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if not queue and temp:
                for i in range(len(temp) - 1):
                    temp[i].nextRight = temp[i + 1]
                queue = deque(temp)
                temp = []
        return root
                
        


