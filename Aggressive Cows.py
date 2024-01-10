#User function Template for python3

class Solution:
    def canWePlace(self,stalls, dist, cows):
        n = len(stalls)  # size of array
        cntCows = 1  # no. of cows placed
        last = stalls[0]  # position of last placed cow
        for i in range(1, n):
            if stalls[i] - last >= dist:
                cntCows += 1  # place next cow
                last = stalls[i]  # update the last location
        if cntCows >= cows:
            return True
        return False
    def solve(self,n,k,stalls):
        n = len(stalls)  # size of array
        stalls.sort()  # sort the stalls
        low = 1
        high = stalls[n - 1] - stalls[0]
    # apply binary search
        while low <= high:
            mid = (low + high) // 2
            if self.canWePlace(stalls, mid, k):
                low = mid + 1
            else:
                high = mid - 1
        return high
        
