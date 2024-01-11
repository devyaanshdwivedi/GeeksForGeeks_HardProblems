from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        visited = [0]*V
        
        ans = False
        def solve(node,prevNode):
            
            if visited[node]:
                return True
            visited[node] = 1
            for x in adj[node]:
                if x == prevNode:
                    continue
                if solve(x, node):
                    return True
            return False
        for i in range(V):
            if visited[i] == 0:
                if solve(i,-1):
                    return True
        return False