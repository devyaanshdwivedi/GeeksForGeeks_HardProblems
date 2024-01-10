#User function Template for python3
class Solution:
    
    def constructLowerArray(self,arr, n):
        # code here
        ans=[]
        res=[]
        n=len(arr)
        for i in range(n-1,-1,-1):
            l=0
            r=len(res)-1
            while l<=r:
                mid=(l+r)//2
                if res[mid] > arr[i]:
                    r=mid-1
                elif res[mid]<arr[i]:
                    l=mid+1
                else:
                    r=mid-1
            res.insert(l,arr[i])   
            ans.append(l)
        return ans[::-1]