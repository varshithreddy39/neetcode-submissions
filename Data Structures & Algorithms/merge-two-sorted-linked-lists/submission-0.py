# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ans = None
        tail = None

        i = list1
        j = list2

        while i and j:
            if i.val > j.val:
                node = j
                j = j.next
            else:
                node = i
                i = i.next
            if ans is None:
                ans = node
                tail = node
            else:
                tail.next = node
                tail = tail.next

        if i:
            if ans is None:
                ans = i
            else:
                tail.next = i

        if j:
            if ans is None:
                ans = j
            else:
                tail.next = j

        return ans
        