# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        #find middle node
        #set slow and fast pointer
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        cur,prev=slow.next,None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        slow.next=None
        head1,head2=head,prev
        while head2:
            temp=head1.next
            head1.next=head2
            head1=head2
            head2=temp
        return head
            
        
        
        
        
        
        
        
        
        
        
        
        
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
        
#         #reverse the second half
#         #to reverse we need three things
#         prev,cur=None,slow.next #second half 
#         while cur:
#             temp=cur.next
#             cur.next=prev
#             prev=cur
#             cur=temp
#         slow.next=None
#         #now mix 1st half with second half(reverse)
#         head1,head2=head,prev
#         while head2:
#             temp=head1.next
#             head1.next=head2
#             head1=head2
#             head2=temp
#         return head
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         list1=head
#         slow=head
#         fast=head.next
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#         list2=slow.next
#         slow.next=None
        
#         prev=None
#         while list2:
#             nxt=list2.next
#             list2.next=prev
#             prev=list2
#             list2=nxt
#         list2=prev
        
#         while list1 and list2:
#             temp1=list1.next
#             temp2=list2.next
#             list1.next=list2
#             list2.next=temp1
#             list1=temp1
#             list2=temp2
#         return head
