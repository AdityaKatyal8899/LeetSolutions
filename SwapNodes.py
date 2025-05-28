from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        curr = head
        new = head.next

        while curr.next:
            new = curr.next
            curr.next = new.next
            new.next = curr
            if prev:
              prev.next = new
            else:
              head = new
            prev = curr
            curr = curr.next
        return head


