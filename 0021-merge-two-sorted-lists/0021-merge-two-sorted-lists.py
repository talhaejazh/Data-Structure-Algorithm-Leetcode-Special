class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        cur=dummy
        print(dummy.next)
        
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next=ListNode(list1.val)
                list1=list1.next
            else:
                cur.next=ListNode(list2.val)
                list2=list2.next
            cur=cur.next
        
        while list1:
            cur.next=ListNode(list1.val)
            list1=list1.next
            cur=cur.next
        while list2:
            cur.next=ListNode(list2.val)
            list2=list2.next
            cur=cur.next
        return dummy.next
