#User function Template for python3


class Solution:
    def chooseandswap (self, A):
        # code here
        # time -- O(26 * n):
        # space -- O(26*n)
        
        ans = []
        arr = [-1]*26
        
        for i in range(len(A)):
            ans.append(A[i])
            idx = ord(A[i]) - ord("a")
            if arr[idx] == -1:
                arr[idx] = i
        
        char1 = "X"
        Char2 = "X"
        for i in range(len(A)):
            idx = ord("a")
            flag = False
            
            while idx < ord(A[i]):
                if arr[idx - ord("a")] > i:
                    char1 = chr(idx)
                    char2 = A[i]
                    flag = True
                    break
                
                idx += 1
            
            if flag:
                break
            
        if char1 != "X":
            for i in range(len(A)):
                if ans[i] == char1:
                    ans[i] = char2
                
                elif ans[i] == char2:
                    ans[i] = char1
        
        return "".join(ans)



