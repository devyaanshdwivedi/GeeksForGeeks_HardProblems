#User function Template for python3

class Solution:
    def minTime(self, root, target):
        que = []
        mp = {}
        node = None
        mp[root] = None
        que.append (root)
        while (len (que) > 0):
            size = len (que)
            for _ in range (size):
                temp = que.pop(0)
                if (temp.data == target):
                    node = temp
                if (temp.left is not None):
                    mp[temp.left] = temp
                    que.append (temp.left)
                if (temp.right is not None):
                    mp[temp.right] = temp
                    que.append (temp.right)
        visited = set()
        ans = 0
        que.append (node)
        visited.add (node)
        while (len (que) > 0):
            size = len (que)
            more = False
            for _ in range (size):
                temp = que.pop(0)
                if (temp.left is not None and temp.left not in visited):
                    more = True
                    que.append (temp.left)
                    visited.add (temp.left)
                if (temp.right is not None and temp.right not in visited):
                    more = True
                    que.append (temp.right)
                    visited.add (temp.right)
                if (mp[temp] is not None and mp[temp] not in visited):
                    more = True
                    que.append (mp[temp])
                    visited.add (mp[temp])
            if (more):
                ans += 1
        return ans