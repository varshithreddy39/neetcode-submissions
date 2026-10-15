# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while minHeap:
            value, i, node = heapq.heappop(minHeap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        tail.next = None
        return dummy.next