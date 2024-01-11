#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    timer = 1
    def dfs(self,node,parent,vis,adj,tin,low,mark):
        vis[node] = 1
        tin[node]  = low[node] = self.timer
        self.timer += 1
        child = 0
        for i in adj[node]:
            if i == parent:
                continue
            if not vis[i]:
                self.dfs(i,node,vis,adj,tin,low,mark)
                low[node] = min(low[node],low[i])
                if(low[i]>=tin[node] and parent != -1):
                    mark[node] = 1
                child += 1
            else:
                low[node] = min(low[node],tin[i])
                
        if child>1 and parent == -1:
            mark[node] = 1
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, n, adj):
        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        mark = [0] * n
        for i in range(n):
            if not vis[i]:
                self.dfs(0,-1,vis,adj,tin,low,mark)
        ans = []        
        for i in range(n):
            if mark[i] == 1:
                ans.append(i)
        if len(ans) == 0:
            return [-1]
        return ans 
