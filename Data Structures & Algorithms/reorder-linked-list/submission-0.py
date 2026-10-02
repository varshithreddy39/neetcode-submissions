# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        l2=slow.next
        slow.next = None
        prev=None
        curr=l2

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        l1,l2=head,prev

        while l2:
            temp1,temp2=l1.next,l2.next
            l1.next=l2
            l2.next=temp1
            l1,l2=temp1,temp2


        