from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def merge_linked_lists(l1, l2):
          dummy = ListNode()
          tail = dummy

          while l1 and l2:
              if l1.val < l2.val:
                  tail.next = l1
                  l1 = l1.next
              else:
                  tail.next = l2
                  l2 = l2.next
              tail = tail.next

          tail.next = l1 if l1 else l2
          return dummy.next

    # Helper functions for testing
    def list_to_linked(lst):
        dummy = ListNode()
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def linked_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    return linked_to_list(merge_linked_lists(list_to_linked(list1), list_to_linked(list2)))
  

list1 = [1, 3, 5]
list2 = [2, 4, 6]

# Convert lists to linked lists
s = Solution()
print(s.mergeTwoLists(list1, list2))




