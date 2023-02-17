class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        if slow == fast:
            return True
        
        return False
