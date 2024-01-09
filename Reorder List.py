#User function Template for python3

#User function Template for python3

# Node Class    

class Solution:
    
    def reverse(self,h):
        if not h or not h.next:
            return h
        ptr = None
        while h:
            temp = h.next
            h.next = ptr
            ptr = h
            h = temp
        return ptr
    
    def rex(self,head):
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            slow = slow.next
        ex = slow.next
        slow.next = None
        return ex
        
    def reorderList(self,head):
        h = self.rex(head)
        h = self.reverse(h)
        p = head
        while h:
            x = h.next
            h.next = p.next
            p.next = h
            p = p.next.next
            h = x
        return head


# } Driver Code Ends