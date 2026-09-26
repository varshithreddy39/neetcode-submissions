# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==1:
            return head.next

        temp=head
        count=0

        while temp:
            if count==n-1:
                temp.next=temp.next.next
            temp=temp.next
            count+=1
        return head
