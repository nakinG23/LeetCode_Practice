# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class singlyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()  # Dummy node to simplify result list construction
        current = dummy_head
        carry = 0  # To store carry value

        while l1 or l2 or carry:
            # Get values from the current nodes, or 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Compute the sum of values and carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for the next digit
            current.next = ListNode(total % 10)  # Store the single digit

            # Move to the next nodes
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next  # Return the result list (skipping dummy head)

# Create the first linked list (l1 = [2,4,3] representing 342)
l1 = singlyLinkedList()
l1.append(2)
l1.append(4)
l1.append(3)

# Create the second linked list (l2 = [5,6,4] representing 465)
l2 = singlyLinkedList()
l2.append(5)
l2.append(6)
l2.append(4)

# Use the Solution class to add the two numbers
solution = Solution()
result = solution.addTwoNumbers(l1.head, l2.head)

# Traverse and print the result linked list
current = result
while current:
    print(current.val, end=" -> ")
    current = current.next
# Output: 7 -> 0 -> 8 ->