# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy

        while True:
            
            temp = prev_group_tail.next
            count = 0

            while temp and count < k:
                temp = temp.next
                count += 1

            
            if count < k:
                break

            
            group_head = prev_group_tail.next
            next_group = temp

            
            prev = next_group
            curr = group_head

            while curr != next_group:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            
            prev_group_tail.next = prev

            
            prev_group_tail = group_head

        return dummy.next



        