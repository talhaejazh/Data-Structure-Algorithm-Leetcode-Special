# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        # slow=dummy
        # fast=head
        slow=fast=dummy
        for _ in range(n):
            fast=fast.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next
        
        
        
        
        
        
#         print(fast)
#         while n:
#             fast=fast.next
#             n-=1
#         while fast:
#             slow=slow.next
#             fast=fast.next
#         slow.next=slow.next.next
#         return dummy.next
        