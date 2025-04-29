from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()  # Dummy node to build the new list
        tail = dummy  # Tail always points to the last node in the merged list

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Move the tail pointer

        # Attach the remaining part (only one of these will be non-empty)
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next  # The merged list starts from dummy.next