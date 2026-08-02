# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tz = 0

        result = ListNode()
        h = result

        # loop to make additions
        while l1 != None or l2 != None:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            r = v1 + v2 + tz

            h.next = ListNode(r%10)
            h = h.next

            tz = r//10

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if tz:
            h.next = ListNode(tz)


        return result.next

        


