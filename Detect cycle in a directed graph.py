#User function Template for python3


class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, v, adj):
        visited = set() 
        def dfs(curr,recStack):
            visited.add(curr)
            recStack.add(curr)
            for nbr in adj[curr]:
                if nbr not in visited:
                    if dfs(nbr,recStack):
                        return True
                elif nbr in recStack:
                    return True
            recStack.remove(curr)
            return False
        
        
        for i in range(v):
            if i not in visited:
                recStack = set()
                if dfs(i,recStack):
                    return True
        return False
