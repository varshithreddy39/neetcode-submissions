# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i=l1
        j=l2


        dummy=ListNode(0)
        temp=dummy
        carry=0

        while i or j or carry:
            total=carry

            if i:
                total += i.val
                i = i.next
            if j:
                total += j.val
                j = j.next
            carry = total // 10
            digit = total % 10

            temp.next = ListNode(digit)
            temp = temp.next
        return dummy.next

        