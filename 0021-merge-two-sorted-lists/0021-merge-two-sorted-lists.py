class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1=list1
        l2=list2
        current=dummy=ListNode(0)
        if not l1:
            return l2
        if not l2:
            return l1
        
        while l1 and l2:
            if l1.val<l2.val:
                current.next=l1
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next
        if l1:
            current.next=l1
        if l2:
            current.next=l2
        return dummy.next
        
        
        
        
        
#         dummy=ListNode(0)
#         cur=dummy
#         print(dummy.next)
        
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 cur.next=ListNode(list1.val)
#                 list1=list1.next
#             else:
#                 cur.next=ListNode(list2.val)
#                 list2=list2.next
#             cur=cur.next
        
#         while list1:
#             cur.next=ListNode(list1.val)
#             list1=list1.next
#             cur=cur.next
#         while list2:
#             cur.next=ListNode(list2.val)
#             list2=list2.next
#             cur=cur.next
#         return dummy.next
