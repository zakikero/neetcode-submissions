# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headRes = ListNode()
        res = headRes
        while True:
            if list1 == None:
                headRes.next = list2
                break

            elif list2 == None:
                headRes.next = list1
                break

            elif list1.val >= list2.val:
                headRes.next = list2
                list2 = list2.next
                headRes = headRes.next
            else:
                headRes.next = list1
                list1 = list1.next 
                headRes = headRes.next

        return res.next