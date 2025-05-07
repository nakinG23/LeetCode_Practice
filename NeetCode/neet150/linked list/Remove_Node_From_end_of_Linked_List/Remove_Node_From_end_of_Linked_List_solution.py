from typing import List
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy node points to head
        slow = fast = dummy
        
        # Move fast n+1 steps ahead to maintain a gap of n between slow and fast
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both slow and fast together until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Now, slow is just before the node to delete
        slow.next = slow.next.next
        
        return dummy.next